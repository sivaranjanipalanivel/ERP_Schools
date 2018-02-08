# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import cstr
from erpnext.education.api import get_student_group_students


class StudentAttendance(Document):
	def validate(self):
		self.validate_date()
		self.validate_mandatory()
		self.validate_course_schedule()
		self.validate_student()
		self.validate_duplication()
		
	def validate_date(self):
		if self.course_schedule:
			self.date = frappe.db.get_value("Course Schedule", self.course_schedule, "schedule_date")
	
	def validate_mandatory(self):
		if not (self.batch or self.course_schedule):
			frappe.throw(_("""Student Group or Course Schedule is mandatory"""))
	
	def validate_course_schedule(self):
		if self.course_schedule:
			self.batch = frappe.db.get_value("Course Schedule", self.course_schedule, "project")
	
	def validate_student(self):
		if self.course_schedule:
			batch = frappe.db.get_value("Course Schedule", self.course_schedule, "project")
		else:
			batch = self.batch
		student_group_students = [d.student for d in get_student_group_students(batch)]
		if batch and self.student not in student_group_students:
			frappe.throw(_('''Student {0}: {1} does not belong to Student Group {2}'''.format(self.student, self.student_name, batch)))

	def validate_duplication(self):
		"""Check if the Attendance Record is Unique"""
		attendance_records=None
		if self.course_schedule:
			attendance_records= frappe.db.sql("""select name from `tabStudent Attendance` where \
				student= %s and ifnull(course_schedule, '')= %s and name != %s""",
				(self.student, cstr(self.course_schedule), self.name))
		else:
			attendance_records= frappe.db.sql("""select name from `tabStudent Attendance` where \
				student= %s and batch= %s and date= %s and name != %s and \
				(course_schedule is Null or course_schedule='')""",
				(self.student, self.batch, self.date, self.name))
			
		if attendance_records:
			frappe.throw(_("Attendance Record {0} exists against Student {1}")
				.format(attendance_records[0][0], self.student))

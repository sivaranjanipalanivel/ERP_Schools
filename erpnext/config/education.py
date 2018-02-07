from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Lead Management"),
			"items": [
				 {
					"type": "doctype",
					"name": "Lead",
					"description": _("Database of potential customers."),
				},
				{
					"type": "doctype",
					"name": "Opportunity",
					"description": _("Potential opportunities for selling."),
				}	
			]
		},
		{
			"label": _("Admission"),
			"items": [
				{
					"type": "doctype",
					"name": "Student Applicant"
				},
				{
					"type": "doctype",
					"name": "Program Enrollment"
				},
				{
					"type": "doctype",
					"name": "Program Enrollment Tool"
				}
			]
		},
		{
			"label": _("Student"),
			"items": [
				{
					"type": "doctype",
					"name": "Student"
				},
				{
					"type": "doctype",
					"name": "Guardian"
				},
				{
					"type": "doctype",
					"name": "Student Log"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Student and Guardian Contact Details",
					"doctype": "Program Enrollment"
				}

			]
		},
		{
			"label": _("Attendance"),
			"items": [
				{
					"type": "doctype",
					"name": "Student Attendance"
				},
				{
					"type": "doctype",
					"name": "Student Leave Application"
				},
				{
					"type": "doctype",
					"name": "Student Attendance Tool"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Absent Student Report",
					"doctype": "Student Attendance"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Student Batch-Wise Attendance",
					"doctype": "Student Attendance"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Student Monthly Attendance Sheet",
					"doctype": "Student Attendance"
				}
			]
		},
		# {
		# 	"label": _("Schedule"),
		# 	"items": [
		# 		{
		# 			"type": "doctype",
		# 			"name": "Student Group Schedule",
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Course Schedule",
		# 			"route": "List/Course Schedule/Calendar"
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Course Scheduling Tool"
		# 		}
		# 	]
		# },
		{
			"label": _("Couse Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Academic Term"
				},
				{
					"type": "doctype",
					"name": "Academic Year"
				},
				{
					"type": "doctype",
					"name": "Program"
				},
				{
					"type": "doctype",
					"name": "Course"
				},
				{
					"type": "doctype",
					"name": "Project"
				}
			]
		},
		{
			"label": _("Fees Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Fee Category"
				},
				{
					"type": "doctype",
					"name": "Fee Structure"
				},
				{
					"type": "doctype",
					"name": "Fee Schedule"
				},
				{
					"type": "doctype",
					"name": "Fees"
				},
				{
					"type": "doctype",
					"name": "Payment Entry",
					"description": _("Bank/Cash transactions against party or for internal transfer")
				},
				{
					"type": "report",
					"name": "Student Fee Collection",
					"doctype": "Fees",
					"is_query_report": True
				}
			]
		},
		{
			"label": _("Assessment"),
			"items": [
				{
					"type": "doctype",
					"name": "Assessment Plan"
				},
				{
					"type": "doctype",
					"name": "Assessment Schedule"
				},
				{
					"type": "doctype",
					"name": "Assignment"
				},
				{
					"type": "doctype",
					"name": "Assessment Group",
					"link": "Tree/Assessment Group",
				},
				{
					"type": "doctype",
					"name": "Assessment Result"
				},
				{
					"type": "doctype",
					"name": "Assessment Criteria"
				},
				{
					"type": "doctype",
					"name": "Assessment Criteria Group"
				},
				{
					"type": "doctype",
					"name": "Assessment Result Tool"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Course wise Assessment Report",
					"doctype": "Assessment Result"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Assessment Plan Status",
					"doctype": "Assessment Plan"
				},

			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Instructor"
				},
				{
					"type": "doctype",
					"name": "Room"
				},
				{
					"type": "doctype",
					"name": "Student Category"
				},
				{
					"type": "doctype",
					"name": "Branch"
				},
				{
					"type": "doctype",
					"name": "Student Batch Name"
				},
				{
					"type": "doctype",
					"name": "Grading Scale"
				},
				{
					"type": "doctype",
					"name": "Education Settings"
				},
				{
					"type": "doctype",
					"name": "Taxes"
				}
			]
		},
	]

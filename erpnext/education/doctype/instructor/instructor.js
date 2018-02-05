cur_frm.add_fetch("employee", "department", "department");
cur_frm.add_fetch("employee", "image", "image");

frappe.ui.form.on("Instructor", "refresh", function(frm) {
	if(!frm.doc.__islocal) {
		frm.add_custom_button(__("Batch"), function() {
			frappe.route_options = {
				instructor: frm.doc.name
			}
			frappe.set_route("List", "Project");
		});
		frm.add_custom_button(__("Task"), function() {
			frappe.route_options = {
				instructor: frm.doc.name
			}
			frappe.set_route("List", "Task");
		});
		frm.add_custom_button(__("Timesheet"), function() {
			frappe.route_options = {
				instructor: frm.doc.name
			}
			frappe.set_route("List", "Timesheet");
		});
		frm.add_custom_button(__("Course Schedule"), function() {
			frappe.route_options = {
				instructor: frm.doc.name
			}
			frappe.set_route("List", "Course Schedule");
		});
		frm.add_custom_button(__("As Examiner"), function() {
			frappe.route_options = {
				examiner: frm.doc.name
			}
			frappe.set_route("List", "Assessment Plan");
		}, __("Assessment Plan"));
		frm.add_custom_button(__("As Supervisor"), function() {
			frappe.route_options = {
				supervisor: frm.doc.name
			}
			frappe.set_route("List", "Assessment Plan");
		}, __("Assessment Plan"));
	}
});

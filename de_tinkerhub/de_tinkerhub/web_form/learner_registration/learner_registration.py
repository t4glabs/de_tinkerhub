import frappe

def get_context(context):
	# let doc = frappe.db.get_doc('Learner', frappe.session.user)

	context.show_sidebar = 1
	context.no_cache = 1
	return context

import frappe
def get_context(context):
    event_id = frappe.form_dict.name
    event = frappe.get_doc("Tinkerub Event", event_id)
    context.event = event
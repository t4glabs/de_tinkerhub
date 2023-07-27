import frappe
def get_context(context):
    event_id = frappe.form_dict.name
    print(f'\n\n\n {event_id} \n\n')
    event = frappe.get_doc("Tinkerub Event", event_id)
    context.event = event
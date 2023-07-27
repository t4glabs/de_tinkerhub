import frappe
from frappe import get_doc
def get_context(context):
    event_id = frappe.form_dict.name
    event  = get_doc('TinkerHub Event', event_id)
    title = event.title
    print(f'\n\n\n {title} \n\n\n')
    registrants = frappe.db.get_list(
        'Event Registration', 
        filters={
            'event': event_id
        },
        fields=['email'])

    
    context.event = event
    context.registrants = registrants
    context.show_sidebar = 1
    return context
    # print(f'\n\n\n {event_id} \n\n\n')
    # print(f'\n\n\n {event} \n\n\n')
    # context.event = event
    
    # 
    
import frappe
from frappe import get_doc
def get_context(context):
    event_id = frappe.form_dict.name
    event  = get_doc('TinkerHub Event', event_id)
    title = event.title
    learner = []
    guests = []
    print(f'\n\n\n {title} \n\n\n')
    registrants = frappe.db.get_list(
        'Event Registration', 
        filters={
            'event': event_id
        },
        fields=['email', 'is_participant', 'add_skill'],
        order_by = 'is_participant DESC'
        )

    for registrant in  registrants:
        if frappe.db.exists('Learner', registrant.email):
            learner.append(registrant.email)
        else:
            guests.append(registrant.email)
    
    
    context.event = event
    context.registrants = registrants
    # context.learner = learner
    # context.guests = guests
    context.show_sidebar = 1
    context.no_cache = 1
    return context
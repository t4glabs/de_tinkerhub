import frappe
import datetime

def get_context(context):

    context.show_sidebar = 1

    cur_user = frappe.session.user
    
    if cur_user=="Guest":
        frappe.throw( ("You have to login as a member access this page"), frappe.PermissionError)
    else:
        # participated events
        learner = frappe.get_doc("Learner", cur_user)
        event_ids = [event.event for event in learner.my_events]

        context.past_events = frappe.db.get_list('TinkerHub Event',
                                    filters={
                                        'name': ['in', event_ids]
                                    },
                                    fields=['name','title', 'date'])
        # registered events
        registered_event_ids = frappe.get_all(
            'Event Registration',
            filters={
                'email': cur_user
            },
            fields=['event'],
            as_list=True 
        )
        today = datetime.date.today()
        event_ids = [event[0] for event in registered_event_ids]
        context.registered_events = frappe.db.get_list('TinkerHub Event',
                                    filters={
                                        'name': ['in', event_ids],
                                        'starting_date':  (">", today),
                                        'status': ['!=', 'Completed']
                                    },
                                    fields=['name','title', 'date'])

    return context


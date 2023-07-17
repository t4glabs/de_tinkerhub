import frappe

def get_context(context):

    cur_user = frappe.session.user
    
    if cur_user=="Guest":
        frappe.throw( ("You have to login as a member access this page"), frappe.PermissionError)
    else:
        participated_events = frappe.get_all(
            'Event Participant',
            filters={
                'participant_email': cur_user
            },
            fields=['event_id'],
            as_list=True 
        )
        event_ids = [event[0] for event in participated_events]

        context.events = frappe.db.get_list('TinkerHub Event',
                                    filters={
                                        'name': ['in', event_ids]
                                    },
                                    fields=['name','title', 'date'])

    return context


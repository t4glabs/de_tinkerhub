import frappe
import datetime

def get_context(context):

    user_roles = frappe.get_roles()
    if 'Event Admin' in user_roles:
        context.event_admin = True
    else:
        context.event_admin = False

    today = datetime.date.today()
    context.events = frappe.db.get_list('TinkerHub Event',
                                filters={
                                    'starting_date':  [">=", today],
                                    'status': 'Confirmed',
                                    'is_published': 1
                                },
                                fields=['name','title', 'starting_date'])
    
    context.show_sidebar = 1
    context.no_cache = 1
    return context


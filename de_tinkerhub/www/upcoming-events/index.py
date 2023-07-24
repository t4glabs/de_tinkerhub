import frappe
import datetime

def get_context(context):

    today = datetime.date.today()
    context.events = frappe.db.get_list('TinkerHub Event',
                                filters={
                                    'starting_date':  (">", today),
                                    'status': ['!=', 'Completed'],
                                    'is_published': 1
                                },
                                fields=['name','title', 'starting_date'])
    
    context.show_sidebar = 1
    return context


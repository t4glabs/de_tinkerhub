import frappe
import datetime

def get_context(context):

    today = datetime.date.today()
    context.events = frappe.db.get_list('TinkerHub Event',
                                filters={
                                    'date':  (">", today)
                                },
                                fields=['name','title', 'date'])
    
    context.show_sidebar = 1
    return context


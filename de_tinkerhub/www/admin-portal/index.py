import frappe

roles = frappe.get_roles()

cur_user = frappe.session.user
if cur_user == 'Guest' or 'Event Admin' not in roles:
    frappe.throw( ("You have to login as an Event Admin to access this page"),frappe.PermissionError)
else: 
    def get_context(context):
        context.events = frappe.db.get_list('TinkerHub Event',
                                filters={
                                    'owner':  cur_user
                                },
                                fields=['name','title', 'starting_date'])
        context.show_sidebar = 1
        return context




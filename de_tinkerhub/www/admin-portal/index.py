import frappe

roles = frappe.get_roles()
cur_user = frappe.session.user

if  (cur_user == 'Guest' or 'Event Admin' not in roles) and cur_user != 'Administrator':
    frappe.throw( ("You have to login as an Event Admin to access this page"),frappe.PermissionError)
    event_admin = False
else: 
    def get_context(context):

        event_admin = True

        college = frappe.db.get_value('Learner', cur_user, 'college')

        if college:
           admins = frappe.db.get_list('Learner',
                               filters={
                                   'college': college
                               },
                               fields=['email'],
                               as_list=True 
                               )
           college_admins = [admin[0] for admin in admins ]
           
           context.events = frappe.db.get_list('TinkerHub Event',
                                    filters = {
                                        'owner': ['in', college_admins]
                                    },
                                    fields=['name','title', 'starting_date']
                                    )
        else:
            context.events = frappe.db.get_list('TinkerHub Event',
                                    filters={
                                        'owner':  cur_user
                                    },
                                    fields=['name','title', 'starting_date'])
           
        context.show_sidebar = 1
        context.no_cache = 1
        context.event_admin = event_admin
        return context




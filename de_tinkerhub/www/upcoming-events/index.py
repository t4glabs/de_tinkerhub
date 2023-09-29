import frappe
import datetime

def get_context(context):

    user_roles = frappe.get_roles()
    if 'Event Admin' in user_roles:
        context.event_admin = True
    else:
        context.event_admin = False
    
    
    events = []
    # college = frappe.db.get_value('Learner', frappe.session.user, 'college')

    # query = frappe.db.sql_list(f"""
    # SELECT te.name
    # FROM `tabTinkerHub Event` as te
    # WHERE 
    #     starting_date >= CURDATE() AND
    #     status = 'Confirmed' AND
    #     is_published = 1 AND
    #     public_event = 1
    # UNION
   
    # SELECT e.name
    # FROM `tabTinkerHub Event` e
    # INNER JOIN `tabLearner` l ON e.host_college = l.college
    # WHERE
    #     e.starting_date >= CURDATE() AND
    #     e.status = 'Confirmed' AND
    #     e.is_published = 1 AND
    #     e.public_event = 0 AND
    #     l.name = '{frappe.session.user}';

    # """)
    query = frappe.db.sql_list(f"""
    SELECT te.name
    FROM `tabTinkerHub Event` as te
    WHERE 
        starting_date >= CURDATE() AND
        status = 'Confirmed' AND
        is_published = 1 AND
        (public_event = 1 OR host_college IN (
            SELECT college FROM `tabLearner` WHERE name = '{frappe.session.user}'
        ));

    """)


    if query:
        events = frappe.db.get_list(
			'TinkerHub Event',
			filters = {
				'name': ['in', query]
			},
			fields = ['name','starting_date', 'title', 'host_college']
    	)

    print(f'\n\n\n events: \n {query} \n\n\n ')
    context.events = events
    context.show_sidebar = 1
    context.no_cache = 1
    return context


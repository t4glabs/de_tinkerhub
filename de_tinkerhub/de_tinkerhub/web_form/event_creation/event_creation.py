import frappe
def get_context(context):
	context.no_cache = 1
	return context

cur_user = frappe.session.user
user_roles = frappe.get_roles()

@frappe.whitelist()
def check_admin():
	list = []
	if 'Event Admin' in user_roles: 
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
			
			events = frappe.db.get_list('TinkerHub Event',
						filters = {
							'owner': ['in', college_admins]
						},
						fields=['name','title', 'starting_date']
					)
			list = [event.name for event in events ]
			
		else:
			events = frappe.db.get_list('TinkerHub Event',
						filters = {
							'owner': cur_user
						},
						fields=['name','title', 'starting_date'])
			list = [event.name for event in events]
	else:
		list = []

	return list
	
	
	

# [item['name'] for sublist in data_dict.values() for item in sublist]
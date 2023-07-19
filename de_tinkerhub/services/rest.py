import frappe

@frappe.whitelist()
def learner_registrant(event, learner, email):

    # print(f'\n\n\n\n { data } \n\n\n\n')

    # learner = frappe.db.get_value('User', f'{ email }', ['full_name'])

    registration = frappe.get_doc({
        "doctype": "Event Registration",
        "email": f'{email}',
        "learner": f'{learner}',
        "event": f'{event}'
    })
    # add invoice record to databse
    registration.insert(ignore_permissions = True).save()
    # frappe.db.commit()

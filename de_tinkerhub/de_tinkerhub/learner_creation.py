import frappe
from frappe import get_doc
import random

def on_user_signup(doc, method):
    user_id = doc.email
    print(f'\n\n\n NEW USER SIGNUP- {user_id} \n\n\n')
    # user_id = doc.email

    if not frappe.db.exists({"doctype":"Learner","user": user_id}):
        learner = get_doc({
            "doctype": "Learner",
            "mail": user_id,
            "email": user_id,
            "is_published": 1
        })
        learner.save(ignore_permissions=True)
        frappe.db.commit()
        user_doc = get_doc('User', user_id)
        # assign learner role      
        user_doc.append('roles', {
            'role': 'Learner'
        })
        user_doc.save(ignore_permissions=True)
        frappe.db.commit()
        permission = get_doc({
            "doctype": "User Permission",
            "user": user_id,
            "allow": 'Learner',
            "for_value": doc.email
        })
        permission.save(ignore_permissions=True)
        
        frappe.db.commit()
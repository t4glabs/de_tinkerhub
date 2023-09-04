import frappe
from frappe import get_doc
import random

def on_user_signup(doc, method):
    user_id = doc.name

    if not frappe.db.exists({"doctype":"Learner","user": user_id}):
        learner = get_doc({
            "doctype": "Learner",
            "mail": user_id,
            "email": user_id,
            "is_published": 1
        })
        learner.save(ignore_permissions=True)
        permission = get_doc({
            "doctype": "User Permission",
            "user": user_id,
            "allow": 'Learner',
            "for_value": user_id
        })
        permission.save(ignore_permissions=True)
        # assign learner role
        user_doc = get_doc('User', user_id)
        user_doc.append('roles', {
            'role': 'Learner'
        })
        user_doc.save(ignore_permissions=True)
        frappe.db.commit()
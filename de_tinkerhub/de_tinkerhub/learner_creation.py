import frappe
from frappe import get_doc

def on_user_signup(doc, method):
    user_id = doc.name
    if not frappe.db.exists({"doctype":"Learner","user": user_id}):
        learner = get_doc({
            "doctype": "Learner",
            "user": user_id,
            "is_published": 1
        })
        learner.save(ignore_permissions=True)
        # assign learner role
        user_doc = get_doc('User', user_id)
        user_doc.append('roles', {
            'role': 'Learner'
        })
        user_doc.save(ignore_permissions=True)
        frappe.db.commit()



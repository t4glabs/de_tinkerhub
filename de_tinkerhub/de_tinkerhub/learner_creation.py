import frappe
from frappe import get_doc

def on_user_signup(doc, method):
    user_id = doc.name
    if not frappe.db.exists({"doctype":"Learner","user": user_id}):
        learner = get_doc({
            "doctype": "Learner",
            "user": user_id
        })
        learner.save(ignore_permissions=True)



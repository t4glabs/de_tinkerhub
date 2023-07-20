import frappe

@frappe.whitelist(allow_guest=True)
def event_registration(event, email, full_name, mobile_no):


    registration = frappe.get_doc({
        "doctype": "Event Registration",
        "event":  event,
        "email": email,   
        "full_name": full_name,
        "mobile_no": mobile_no
    })

    registration.insert(ignore_permissions = True).save()
    # frappe.db.commit()
    frappe.msgprint(
        msg='Thank you for registering!',
        title='Success'
    )
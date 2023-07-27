import frappe
from frappe import get_doc

@frappe.whitelist(allow_guest=True)
def event_registration(event, email, full_name, mobile_no):
    if frappe.db.exists("Event Registration", {"event": event, "email": email}):
        frappe.msgprint(
            msg='You are already registered',
            title='Notification'
        )
    else:
        registration = get_doc({
            "doctype": "Event Registration",
            "event":  event,
            "email": email,
            "full_name": full_name,
            "mobile_no": mobile_no
        })

        registration.save(ignore_permissions = True)
        frappe.msgprint(
            msg='Thank you for registering!',
            title='Success'
        )

@frappe.whitelist(allow_guest=True)
def submit_feedback(event, learner, question, response):

    feedback = get_doc({
        "doctype": "Feedback Submission",
        "event": event,
        "learner": learner,
        "question": question,
        "user_response": response
    })

    feedback.insert(ignore_permissions = True).save()
    # frappe.db.commit()
    frappe.msgprint(
        msg='Thank you for your feedback!',
        title='Success'
    )

@frappe.whitelist(allow_guest=True)
def submit_assignment(event, learner, question, response):

    assignment = get_doc({
        "doctype": "Assignment Submission",
        "event": event,
        "learner": learner,
        "question": question,
        "user_response": response
    })

    assignment.insert(ignore_permissions = True).save()
    # frappe.db.commit()
    frappe.msgprint(
        msg='Your assignment has been submitted.',
        title='Success'
    )

@frappe.whitelist(allow_guest=True)
def part(emails):
    print(f'\n\n\n Get a job :) \n\n\n')
    print(f'\n\n\n {emails} \n\n\n')

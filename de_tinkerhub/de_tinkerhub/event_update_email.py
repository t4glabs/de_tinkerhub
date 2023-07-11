import frappe

def send_event_update_email(doc, method):
    event_name = doc.name
    registrations = frappe.get_all(
        "Event Registration",
        filters={"event": event_name},
        fields=["learner"]
    )
    subject = "Event Update: {}".format(event_name)
    message = "Dear learner, the event '{}' has been updated.".format(event_name)
    
    for registration in registrations:
        learner = frappe.get_doc("Learner", registration.learner)
        email = learner.email
        frappe.sendmail(recipients=email, subject=subject, message=message)

import frappe
from frappe import _
def get_context(context):
    context.no_cache = 1
    if frappe.session.user == "Guest":
        message = "Please login to access this page."
        raise frappe.PermissionError(_(message))
    context.duplication = False
    if frappe.db.exists("Learner", {"email":frappe.session.user}):
        if frappe.db.exists("Event Registration", {'email':frappe.session.user,
                                                   'event':frappe.form_dict["event"]}):
            context.duplication = True
    else:
        message = "Become a learner to register for event!"
        raise frappe.PermissionError(_(message))

    if frappe.form_dict.get("event"):
        event = frappe.get_doc("TinkerHub Event", frappe.form_dict["event"])
        rq = None
        if frappe.db.exists("Registration Question", {'event':frappe.form_dict["event"]}):
            rq = frappe.get_doc("Registration Question", {'event':frappe.form_dict["event"]})
            fields = ["name", "question", "type", "option_1", "option_2", "option_3", "option_4",
                    "multi_answer_1",  "multi_answer_2",  "multi_answer_3",  "multi_answer_4"]
            questions = frappe.db.get_list("Event Question", {'parent':rq.name}, fields, ignore_permissions=True, order_by="idx")
        context.show_question = True
        context.quiz = {
            "title": event.title,
            "name":rq.name,
            "event_name":frappe.form_dict["event"],
            "questions": questions
        }
    else:
        context.quiz = {}
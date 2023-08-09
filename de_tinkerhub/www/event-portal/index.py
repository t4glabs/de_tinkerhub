import frappe
from frappe import get_doc
import urllib.parse
def get_context(context):
    event_id = frappe.form_dict.name
    event  = get_doc('TinkerHub Event', event_id)

    registrants = frappe.db.get_list(
        'Event Registration', 
        filters={
            'event': event_id
        },
        fields=['name', 'email', 'is_participant', 'add_skill'],
        order_by = 'is_participant DESC'
    )

    learner = []
    guests = []
    final_array = []
    
    # submissions = frappe.get_all('Event Registration', filters={'event': event_id}, fields=['email'])
    # print(f'\n\n\n {submissions} \n\n\n')

    if registrants:
        for submission in registrants:
            print(f'\n\n\n submission: {submission} \n\n\n')
            user_array = []
        # Access the child table field
            user_array = [submission.email, {}]
        
            # print(f'\n\n\n {user_array} \n\n\n')

            # context.has_custom = True
            # rq = frappe.get_doc("Event Registration", {'event':frappe.form_dict.name, 'email': submission.email})
            rq = frappe.db.get_value('Event Registration', {'event':frappe.form_dict.name, 'email': submission.email}, ['name'])
            print(f'\n\n\n rq-name: {rq} \n\n\n')
            fields = ["name", "question", "answer_1"]
            qa = frappe.db.get_list("Registration Quiz Answer", {'parent':rq}, fields, ignore_permissions=True, order_by="idx")
            
            # rows = submission.registration_quiz_answer

            # Loop through child table rows
            if qa:
                for q in qa:
                    question = q.question
                    # answer = urllib.parse.unquote(q.answer_1)
                    answer = q.answer_1
                    print(f'\n\n\n {answer} \n\n\n')
                    user_array[1][f'{question}'] = f'{answer}'
            else:
                print(f'\n\n\n no qa \n\n\n')
            final_array.append(user_array)

            
        
    print(f'\n\n\n {final_array} \n\n\n')
    context.qa = final_array
            
    
    parents = [parent.name for parent in registrants]

    print(f'\n\n\n {parents} \n\n\n')

    context.child_table_data = frappe.db.get_all(
        'Registration Quiz Answer',
        filters={'parent': ['in', parents]},  
        fields=['question', 'answer_1'],  
        order_by='idx'  
    )
    if frappe.db.exists("Registration Question", {'event':frappe.form_dict.name}):
            # context.has_custom = True
            rq = frappe.get_doc("Registration Question", {'event':frappe.form_dict.name})
            fields = ["name", "question", "type"]
            context.questions = frappe.db.get_list("Event Question", {'parent':rq.name}, fields, ignore_permissions=True, order_by="idx")
            # print(f'\n\n\n {questions} \n\n\n')

    
    
    for registrant in  registrants:
        if frappe.db.exists('Learner', registrant.email):
            learner.append(registrant.email)
        else:
            guests.append(registrant.email)
    
    
    context.event = event
    context.registrants = registrants
    # context.learner = learner
    # context.guests = guests
    context.show_sidebar = 1
    context.no_cache = 1
    return context
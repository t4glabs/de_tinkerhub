# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
import json
import ast
from frappe.model.document import Document


class EventRegistration(Document):
			
	def on_update(self):
		existing_skills = []
		if frappe.db.exists("Learner", self.email):
			learner = frappe.get_doc("Learner", self.email)
			existing_skills = [skill.skill for skill in learner.my_skills]
			print(f'\n\n\n ex {existing_skills} \n\n\n')
			existing_event = [event.event for event in learner.my_events]
			#  skills from event
			event = frappe.get_doc("TinkerHub Event", self.event)
			event_skills = [skill.skill for skill in event.skills]

			if self.is_participant:
				if not self.event in existing_event:
					learner_event=learner.append("my_events")
					learner_event.event= self.event
				learner.save(ignore_permissions = True)
			else:
				if self.event in existing_event:
					for row in learner.my_events:
						if row.event == self.event:
							row.delete(ignore_permissions=True)

			if self.add_skill:
				for skill in event_skills:
					if skill not in existing_skills:
						learner.append('my_skills', { 'event': self.event ,'skill': skill})
			else:
				for skill in event_skills:
					for row in learner.my_skills:
						if row.skill == skill:
							row.delete(ignore_permissions=True)
			learner.save(ignore_permissions=True)

			skills = frappe.get_all('My Skills', filters={'parent': learner }, fields=['skill'])
			learner_skills = [skill['skill'] for skill in skills]
			skill_list= ', '.join(learner_skills)
			frappe.db.set_value("Learner", self.email, "skill_list", skill_list)  
			frappe.db.commit()
			
			

@frappe.whitelist(allow_guest=True)
def save_response(result, primary, event):
	prim =  ast.literal_eval(primary)
	result = json.loads(result)
	response = frappe.new_doc("Event Registration")

	response.event = event
	response.full_name = prim[0]
	response.email = prim[1]
	response.mobile_no = prim[2]
	for i in result:
		response.append('registration_quiz_answer',i)
	response.save(ignore_permissions=True)
	return response.name
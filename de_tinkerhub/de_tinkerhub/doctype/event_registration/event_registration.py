# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class EventRegistration(Document):

	def before_insert(self):
		event = frappe.get_doc("TinkerHub Event", self.event)
		for event_skill in event.skills:
			self.append("skills_gained", {
				"skill": event_skill.skill
			})
			
	def on_update(self):
		if frappe.db.exists("Learner", self.email):
			learner = frappe.get_doc("Learner", self.email)
			existing_skills = [skill.skill for skill in learner.my_skills]

			for skills_gained in self.skills_gained:
				if skills_gained.skill in existing_skills:
					if not skills_gained.gained == 1:
						for learner_skill in learner.my_skills:
							if learner_skill.skill == skills_gained.skill:
								learner.my_skills.remove(learner_skill)

				elif skills_gained.gained == 1:
					learner_skill = learner.append("my_skills")
					learner_skill.skill = skills_gained.skill
					learner_skill.event = self.event

			learner.save()

@frappe.whitelist()
def save_response(result, event):
	result = json.loads(result)
	response = frappe.new_doc("Event Registration")
	learner = frappe.get_doc("Learner", {"email":frappe.session.user})
	response.event = event
	response.full_name = learner.full_name
	response.email = learner.email
	response.mobile_no = learner.mobile_no
	for i in result:
		response.append('registration_quiz_answer',i)
	response.save(ignore_permissions=True)
	return response.name
# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
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
			existing_event = [event.event for event in learner.my_events]

			if not self.event in existing_event:
				learner_event=learner.append("my_events")
				learner_event.event = self.event
			learner.save()
	
		

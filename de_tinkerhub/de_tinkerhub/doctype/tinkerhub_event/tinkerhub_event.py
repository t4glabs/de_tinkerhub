# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TinkerHubEvent(Document):
	def on_update(self):
		event_registrations = frappe.get_all("Event Registration", filters={"event": self.name})
		
		for event_registration in event_registrations:
			registration_doc = frappe.get_doc("Event Registration", event_registration.name)
			existing_skills = [skill.skill for skill in registration_doc.skills_gained]
			
			for skill in self.skills:
				if skill.skill not in existing_skills:
					registration_doc.append("skills_gained", {
						"skill": skill.skill
					})
			registration_doc.save()
		
	def validate(self):
		event_registrations = frappe.get_all("Event Registration", filters={"event": self.name})

		for event_registration in event_registrations:
			registration_doc = frappe.get_doc("Event Registration", event_registration.name)
			existing_skills = [skill.skill for skill in registration_doc.skills_gained]

			for existing_skill in existing_skills:
				if existing_skill not in [skill.skill for skill in self.skills]:
					for skill in registration_doc.skills_gained:
						if skill.skill == existing_skill:
							registration_doc.skills_gained.remove(skill)

			registration_doc.save()

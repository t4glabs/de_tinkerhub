# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.utils import cleanup_page_name
from datetime import datetime

class TinkerHubEvent(WebsiteGenerator):
	
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

		# web view route
		if not self.route:
			self.route = f"events/{cleanup_page_name(self.name)}"

	# convert time format
	
	def get_context(self, context):
		# convert time to 12 hour format
		times = [self.starting_time, self.ending_time]
		for index, time in enumerate(times):
			time_obj = datetime.strptime(str(time), "%H:%M:%S")
			context[f"time_{index}"]  = time_obj.strftime("%I:%M %p")

		return context


		


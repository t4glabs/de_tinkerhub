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
			self.route = f"events/{self.name}"

	
	def get_context(self, context):

		user_roles = frappe.get_roles()
		cur_user = frappe.session.user
		participant = False
		cur_event = self.name

		if cur_user == 'Guest':
			is_admin = False
			is_learner = False
			is_guest = True
		elif cur_user == 'Administrator':
			is_admin = True
			is_learner = False
			is_guest = False
		elif 'Learner' in user_roles:
			is_admin = False
			is_learner = True
			is_guest = False

		if is_learner:
			if frappe.db.exists("Learner", cur_user):
				learner = frappe.get_doc("Learner", cur_user)
				user_events = [event.event for event in learner.my_events]
				if cur_event in user_events:
					participant = True
			else:
				participant = False
		# convert time to 12 hour format
		event_time = [self.starting_time, self.ending_time]
		# for index, time in enumerate(event_time):
		# 	if time:
		# 		time_obj = datetime.strptime(str(time), "%H:%M:%S")
		# 		context[f"event_time_{index}"]  = time_obj.strftime("%I:%M %p")

		context.participant = participant
		context.is_guest = is_guest
		context.is_learner = is_learner
		context.is_admin = is_admin
		context.show_sidebar=1

		return context


	



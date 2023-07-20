# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.utils import cleanup_page_name
from datetime import datetime

class TinkerHubEvent(WebsiteGenerator):
	
	def on_update(self):
		cd = frappe.db.get_value('Learner', f'{frappe.session.user}' 'my_events')
		print(f'\n\n\n {cd} \n\n\n')
		if self.assignment_question != None:
			if not frappe.db.exists("Assignment Submission", self.name):
				assignment_question = frappe.get_doc({
					"doctype": "Assignment Submission",
					"event_id": self.name,
					"question": self.assignment_question
				})
				# add invoice record to databse
				assignment_question.insert(ignore_permissions = True).save()
				frappe.db.commit()
			elif frappe.db.exists("Assignment Submission", self.name):
				frappe.db.set_value("Assignment Submission", self.name, "question", self.assignment_question)

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

	
	def get_context(self, context):

		user_roles = frappe.get_roles()

		participant = False
		cur_user = frappe.session.user
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
		
		# convert time to 12 hour format
		event_time = [self.starting_time, self.ending_time]
		for index, time in enumerate(event_time):
			time_obj = datetime.strptime(str(time), "%H:%M:%S")
			context[f"event_time_{index}"]  = time_obj.strftime("%I:%M %p")

		context.participant = participant
		context.is_guest = is_guest
		context.is_learner = is_learner
		context.is_admin = is_admin
		context.show_sidebar=1
		

		return context

		
		# if participant:
		# 	if self.event_status == 'Ongoing':
		# 		if self.assignment_question:
		# 			context.assignment = True
		# 		else:
		# 			context.assignment = False
		# 	else:
		# 		context.assignment = False
			
		# 	if self.event_status == 'Completed':
		# 		if self.assignment_question:
		# 			context.feedback = True
		# 		else:
		# 			context.feedback = False
		# 	else:
		# 		context.feedback = False



		

# feedback question
# if self.feedback_question != None:
# 			if not frappe.db.exists("Feedback Submission", self.name):
# 				feedback_question = frappe.get_doc({
# 					"doctype": "Feedback Submission",
# 					"event_id": self.name,
# 					"question": self.feedback_question
# 				})
# 				# add invoice record to databse
# 				feedback_question.insert(ignore_permissions = True).save()
# 				frappe.db.commit()
# 			elif frappe.db.exists("Feedback Submission", self.name):
# 				frappe.db.set_value("Feedback Submission", self.name, "question", self.feedback_question)
#
# jinjs feedback
# {% if feedback %}
#     <button><a href="{{frappe.utils.get_url()}}/feedback-form/{{name}}/edit">Provide feedback</a></button>
# {% endif %}
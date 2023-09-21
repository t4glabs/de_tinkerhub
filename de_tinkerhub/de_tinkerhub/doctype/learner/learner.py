# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Learner(WebsiteGenerator):

	def get_context(self, context):
		context.show_sidebar = 1
		if self.college:
			context.college_name = frappe.db.get_value('College', self.college, 'college_name') 

	def validate(self):
		if not self.route:
			self.route = f"learner/{self.name}"

	def on_update(self):
	
		if self.college:
			college = self.college
			campus_lead = frappe.get_doc({
				'doctype': 'Learner',
				'filters': {
					'college': college,
					'is_lead': 1
				}
			})		



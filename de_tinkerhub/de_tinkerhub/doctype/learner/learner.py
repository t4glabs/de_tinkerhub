# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Learner(WebsiteGenerator):
	def validate(self):
		# web view route
		if not self.route:
			self.route = f"learner/{self.name}"

	def get_context(self, context):
		
		context.show_sidebar = 1

		cur_user = frappe.session.user
			
		if cur_user == 'Guest':
			context.is_admin = False
			context.is_learner = False
			context.is_guest = True
		elif cur_user == 'Administrator':
			context.is_admin = True
			context.is_learner = False
			context.is_guest = False
		else:
			context.is_admin = False
			context.is_learner = True
			context.is_guest = False

		return context
	




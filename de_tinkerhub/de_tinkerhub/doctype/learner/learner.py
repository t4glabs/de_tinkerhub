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
		return context



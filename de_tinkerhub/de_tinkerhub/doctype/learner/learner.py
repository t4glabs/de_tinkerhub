# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Learner(WebsiteGenerator):
		def validate(self):
			if not self.route:
				self.route = f"learner/{self.mail}"
			if not self.email:
				self.email = self.mail
			if not self.full_name:
				full_name = frappe.db.get_value('User', self.mail, 'full_name')
				self.full_name = full_name

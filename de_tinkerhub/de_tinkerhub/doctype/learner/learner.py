# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Learner(WebsiteGenerator):
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

			if not frappe.db.exists( 'User Permission', { 'user': campus_lead,'allow': 'Learner', 'for_value': self.name }):
				frappe.get_doc({
					'doctype': 'User Permission',
					'user': campus_lead,
					'allow': 'Learner', 
					'for_value': self.name
				})

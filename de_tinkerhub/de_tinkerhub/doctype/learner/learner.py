# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Learner(WebsiteGenerator):
	
	def on_update(self):
		skills = frappe.get_all('My Skills', filters={'parent': self.name }, fields=['skill'])
		learner_skills = [skill['skill'] for skill in skills]
		skill_list= ', '.join(learner_skills)
		frappe.db.set_value("Learner", self.name, "skill_list", skill_list)  
		frappe.db.commit()
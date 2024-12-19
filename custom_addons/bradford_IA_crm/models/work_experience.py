from odoo import models, fields

class WorkExperience(models.Model):
    _name = "bradford.workexperience"
    _description = "Work-Experience"

    name = fields.Char(string="Work-Experience", required=True)
    state = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="State", default="active")

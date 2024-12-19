from odoo import models, fields

class JobTitle(models.Model):
    _name = "bradford.jobtitle"
    _description = "Job-Title"

    name = fields.Char(string="Job-Title", required=True)
    state = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="State", default="active")

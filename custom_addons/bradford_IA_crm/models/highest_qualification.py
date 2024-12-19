from odoo import models, fields

class HighestQualification(models.Model):
    _name = "bradford.highestqualification"
    _description = "Highest-Qualification"

    name = fields.Char(string="Highest-Qualification", required=True)
    state = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="State", default="active")

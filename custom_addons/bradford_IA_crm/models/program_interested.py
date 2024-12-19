from odoo import models, fields

class ProgramInterested(models.Model):
    _name = "bradford.programinterested"
    _description = "Program-Interested"

    name = fields.Char(string="Program-Interested", required=True)
    state = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="State", default="active")

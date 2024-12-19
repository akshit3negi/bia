from odoo import models, fields

class courses(models.Model):
    _name = "bradford.courses"
    _description = "Courses"

    name = fields.Char(string="Courses", required=True)
    state = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="State", default="active")
    # university = fields.Many2one('bradford.university',string="University",required=True)

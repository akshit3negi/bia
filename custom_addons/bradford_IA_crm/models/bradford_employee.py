from odoo import models, fields

class Employee(models.Model):
    _inherit = "hr.employee"

    emp_status = fields.Selection(
        [
            ("active", "Active"),
            ("terminated", "Terminated"),
            ("leave_of_absence", "Leave of Absence"),
        ],
        string="Employee Status",
        required=True,
    )
    reports_to=fields.Many2one('hr.employee',string='Reports To')
    mobile = fields.Char(string='Mobile',required=True)
    im_type = fields.Selection(
        [("google", "Google"), ("yahoo", "Yahoo!"), ("msn", "MSN")],
        string="IM Type",
    )
    im_name=fields.Char(string="IM Name")
    fax=fields.Char(string="Fax")
    notes=fields.Text(string="Notes", required=True)
    address=fields.Char(string="Primary Address")
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.country.state', string='State', domain="[('country_id', '=', country_id)]")
    city=fields.Char(string="City")
    postal_code=fields.Char(string="Postal Code")
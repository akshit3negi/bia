from odoo import models, fields, api
from odoo.tools import format_datetime
from datetime import datetime, timedelta


class call(models.Model):
    _name = "bradford.call"
    _description = "Calling module"

    name = fields.Char(string="Subject", required=True)
    status = fields.Selection(
        [("planned", "Planned"), ("held", "Held"), ("notheld", "Not Held")],
        string="Status",
        default="planned",
        required=True,
    )
    status2 = fields.Selection(
        [("inbound", "Inbound"), ("outbound", "Outbound")],
        string="Status",
        default="inbound",
        required=True,
    )
    relatedto = fields.Many2one("res.partner", string="Related to")

    startdate = fields.Datetime(string="Start Date & Time")
    durationhr = fields.Integer(string="Duration(Hr.)", default="00")
    durationmin = fields.Selection(
        [
            ("0", "00"),
            ("5", "05"),
            ("15", "15"),
            ("25", "25"),
            ("45", "45"),
            ("55", "55"),
        ],
        default="0", string="Duration(Min.)"
    )

    descrip = fields.Text(string="Description")
    assignedto = fields.Many2one("res.users", string="Assigned to")
    createdon = fields.Datetime(
        string="Created On", default=fields.Datetime.now(), readonly=1
    )

    
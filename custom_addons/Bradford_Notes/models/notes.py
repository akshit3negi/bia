from odoo import models, fields
from datetime import datetime

class notes(models.Model):
    _name = "bia.notes"
    _description = "Notes"

    name = fields.Char(string="Subject", required=True)
    contact = fields.Char(string="Contact", required=True)
    relatedto = fields.Selection(
        [("lead", "Lead"), ("emial", "Email")],
        string="Related To", default="Lead")
    
    attach=fields.Binary(string="Attachment", required=True)
    note=fields.Text(string="Note", required=True)
    assignedto=fields.Selection([("admin","Admin"),("rahul","Rahul")], string="Assigned To", default="admin")
    createdby=fields.Char(string="Created by", required=True)

    exit = fields.Datetime(string='Date Current Action',default=datetime.now())
   
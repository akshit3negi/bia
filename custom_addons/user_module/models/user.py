from odoo import fields, models

class user(models.Model):
    _name="module.user"
    _description="User Management Module"
    
    name=fields.Char(string='User Name', required=True)
    email=fields.Char(string="Email", required=True)
    password=fields.Char(string="Password", required=True)
    status=fields.Selection([
        ('active','Active'),
        ('inactive','Inactive')
        ], string="status", default="active")
    role=fields.Selection([
        ('admin','Admin'),
        ('salesexecutive','Sales Executive')
        ], string="role", default="admin")
    
    sd=fields.Date(string="Start Date")
    st=fields.Datetime(string="Start Time")

from odoo import models, fields, api
# from odoo.exceptions import ValidationError
class users(models.Model):
    _name="users.custom"
    _description="This Module is a User API."
    
    name = fields.Char(string="Name", required=True)
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
    
    userpic = fields.Binary(string='Image Attachment')
    # @api.constrains('userpic')
    # def _check_images(self):
    #     for record in self:
    #         if len(record.userpic) < 1:
    #             raise ValidationError("Upload Image.")
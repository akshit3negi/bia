from odoo import api,models, fields
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
import math
class product(models.Model):
    _name="module.product"
    _description="Project management model"
    
    title = fields.Text(string='Product Title', required=True)
    category = fields.Many2one('mymodule.category', string='Category', domain="[('status', '=', 'active')]", required=True)
    subcategory = fields.Many2one('mymodule.subcategory', string='Subcategory', domain="[('category_id', '=', category),('status', '=', 'active')]")
    childcategory = fields.Many2one('mymodule.childcategory', string='ChildCategory', domain="[('subcategory_id', '=', subcategory),('status', '=', 'active')]")
    
    images = fields.Binary(string='Image Attachment')
    images = fields.Many2many('ir.attachment', string="Images", required=True)

    

    # Ensure price and quantity are non-negative
    price = fields.Float(string='Price', required=True, default=1.0, help="Price can not be negative.")
    quantity = fields.Integer(string='Quantity', required=True, default=1, help="Quantity can not be negative.")
    
    @api.onchange('price')
    def _onchange_price(self):
        if math.ceil(self.price) < 1:
            raise UserError("Price cannot be negative or 0.")

    @api.onchange('quantity')
    def _onchange_quantity(self):
        if self.quantity < 1:
            raise UserError("Quantity cannot be negative or 0.")

    # @api.onchange('attachimage')
    # def _onchange_image_ids(self):
    #     if len(self.attachimage) < 1:
    #         raise UserError("You must upload at least one image.")
    #     if len(self.attachimage) > 10:
    #         raise UserError("You cannot upload more than ten images.")
    
    # @api.constrains('attachimage')
    # def _check_image_attachment(self):
    #     for record in self:
    #         if not record.attachimage:
    #             raise ValidationError("You must upload at least 1 image.")
    
    @api.constrains('images')
    def _check_images(self):
        for record in self:
            if len(record.images) < 1 or len(record.images) > 10:
                raise ValidationError("You must upload at least 1 image and at most 10 images.")
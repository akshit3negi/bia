from odoo import fields, api, models


class document(models.Model):
    _name = "bradford.document"
    _description = "Document model"

    name = fields.Char(string="Document Name", requird=True)
    upload = fields.Binary(string="Upload File")
    status = fields.Selection(
        [
            ("active", "Active"),
            ("draft", "Draft"),
            ("faq", "FAQ"),
            ("expired", "Expired"),
            ("underreview", "Under Review"),
            ("pending", "Pending"),
        ],
        string="Status",
        required=True,
        default="active",
    )
    revision = fields.Integer(string="Revision", default=1)
    doctype = fields.Selection(
        [
            ("mailmerger", "Mail Merger"),
            ("eula", "EULA"),
            ("nda", "NDA"),
            ("license", "License Agreement"),
        ],
        string="Document Type",
        default="nda",
    )
    template = fields.Boolean(string="Template?", required=True)
    pubdate = fields.Datetime(string="Publish Date", required=True)
    expdate = fields.Datetime(string="Expiration Date", required=True)
    category = fields.Selection(
        [
            ("marketing", "Marketing"),
            ("knowledgebase", "Knowledge Base"),
            ("sale", "Sales"),
        ],
        string="Category",
        default="sale",
    )
    subcategory = fields.Selection(
        [
            ("collateral", "Marketing Collateral"),
            ("brochures", "Product Brochures"),
            ("faq", "FAQ"),
        ],
        string="Sub-Category",
        default="faq",
    )
    description = fields.Text(string="Description", required=True)
    relateddoc = fields.Many2one("bradford.document", string="Related Document")
    relateddocrevision = fields.Integer(string="Related Documnet Revision", default=1)
    assigned = fields.Many2one("res.partner", string="Assigned To")
    createdon = fields.Datetime(
        string="Created On", default=fields.Datetime.now(), readonly=1
    )

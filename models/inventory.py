from odoo import models, fields, api

class Purchase(models.Model):
    _inherit = 'stock.picking'
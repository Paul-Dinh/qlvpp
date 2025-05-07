from odoo import models, fields, api

class Purchase(models.Model):
    _inherit = 'stock.picking'


internal_transfer_moves_ids = fields.One2many(
        'stock.move', # The target model (Stock Moves)
        'picking_id', # The field on the target model that links back to this model (Stock Picking)
        string='Internal Transfer Moves',
        domain=[('picking_id.picking_type_id', '=', 2)] # The domain to filter the records
    )
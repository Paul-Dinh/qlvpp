from odoo import models, fields, api

class Purchase(models.Model):
    _inherit = 'stock.picking'

    state = fields.Selection(
        selection=[
            ('draft', 'Bản nháp'),
            ('waiting', 'Chờ duyệt'),
            ('assigned', 'Chờ phê duyệt'),
            ('done', 'Đã duyệt'),
            ('cancel', 'Đã hủy'),
            ('confirmed', 'Đã duyệt')
        ],
    )


   # ('draft', 'Draft')
    # ('waiting', 'Waiting Another Operation')
    # ('confirmed', 'Waiting')
    # ('assigned', 'Ready')
    # ('done', 'Done')
    # ('cancel', 'Cancelled')
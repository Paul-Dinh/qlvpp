from odoo import models, fields, api

class Purchase(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection(
        selection=[
            ('draft', 'Đề xuất mua'),
            ('sent', 'Chờ duyệt'),
            ('to approve', 'Chờ phê duyệt'),
            ('purchase', 'Đã duyệt'),
            ('done', 'Đã khóa'),
            ('cancel', 'Đã hủy')
        ],
        string='Trạng thái',
        readonly=True,
        copy=False,
        tracking=True
    )
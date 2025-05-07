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
        
    purchase_id = fields.Many2one(comodel_name='purchase.paper', string='Purchase')

    # def action_cancel(self):
    #     """ Override để ngăn chuyển hướng sau khi hủy phiếu kho """
    #     # Gọi phương thức gốc để thực hiện logic hủy phiếu kho
    #     res = super(Purchase, self).action_cancel()

    #     # Phương thức gốc có thể trả về một dictionary chứa action chuyển hướng.
    #     # Nếu bạn muốn ở lại trang hiện tại, hãy trả về True hoặc một dictionary rỗng.
    #     # Trả về True thường là đủ để Odoo refresh trang hiện tại.
    #     return True
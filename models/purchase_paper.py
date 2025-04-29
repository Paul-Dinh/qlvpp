from odoo import models, fields, api

class PurchasePaper(models.Model):
    _name = 'purchase.paper'

    name = fields.Char(string='Tên')
    date = fields.Date(string='Ngày tạo', default=lambda self: fields.Date.context_today(self),readonly=True)
    paper_ids =fields.One2many(comodel_name='purchase.order', inverse_name='purchase_id', string='Purchase',domain=[('state', 'in', ('sent', 'Chờ duyệt'))])
    paper_count = fields.Integer(string='Số lượng phiếu', compute='_compute_paper_count',readonly=True)
    @api.depends('paper_ids')
    def _compute_paper_count(self):
        for record in self:
            record.paper_count = len(record.paper_ids)


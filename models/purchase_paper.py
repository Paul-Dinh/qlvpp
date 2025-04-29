from odoo import models, fields, api

class PurchasePaper(models.Model):
    _name = 'purchase.paper'

    name = fields.Char(string='Tên')
    date = fields.Date(string='Ngày tạo', default=lambda self: fields.Date.context_today(self),readonly=True)


    paper_ids =fields.One2many(comodel_name='purchase.order', inverse_name='purchase_id', string='Purchase',domain=[('state', 'in', ('purchase', 'Chờ duyệt'))])
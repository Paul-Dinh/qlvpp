from odoo import models, fields, api

class PurchasePaper(models.Model):
    _name = 'inventory.paper'

    name = fields.Char(string='Tên',required=True, index=True)
    date = fields.Date(string='Ngày tạo',default=lambda self: fields.Date.context_today(self), readonly=True, index=True)
    paper_ids = fields.One2many(comodel_name='stock.picking', inverse_name='inventory_paper_id',string='Inventory Transfers', domain=[('state', 'in', ('waiting', 'assigned'))])
    paper_count = fields.Integer(string='Số lượng phiếu', compute='_compute_paper_count',readonly=True)
    @api.depends('paper_ids')
    def _compute_paper_count(self):
        for record in self:
            record.paper_count = len(record.paper_ids)
            


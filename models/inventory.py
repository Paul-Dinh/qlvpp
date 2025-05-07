from odoo import models, fields, api

class Inventory(models.Model):
    _inherit = 'stock.picking'

    state = fields.Selection(
        selection=[
            ('draft', 'Đề xuất nhập'),
            ('waiting', 'Chờ duyệt'),
            ('assigned', 'Chờ phê duyệt'),
            ('done', 'Phê duyệt'),
            ('cancel', 'Đã hủy'),
            ('confirmed', 'Đã duyệt')
        ],
        string='Trạng thái',
        readonly=True,
        copy=False,
        tracking=True,
    )
    inventory_paper_id = fields.Many2one(comodel_name='inventory.paper', string='Tờ trình nhập kho')
    picking_type_id = fields.Many2one(
        'stock.picking.type',
        string='Operation Type',
        default=lambda self: self.env.ref('stock.picking_type_in').id,
         readonly=True
    )

    # @api.model
    # def create(self, vals):
    #     # Gán giá trị mặc định nếu chưa được gán từ trước
    #     if 'picking_type_id' not in vals:
    #         vals['picking_type_id'] = self.env.ref('stock.picking_type_in').id
    #     return super(Inventory, self).create(vals)
    # @api.model
    # def create(self, vals):
    #     picking = super(Inventory, self).create(vals)
    #     if picking.picking_type_id.code == 'incoming':
    #         picking.action_confirm()  # Tự động chuyển sang "Chờ phê duyệt"
    #     return picking
    @api.model
    def create(self, vals): 
        # Gán giá trị mặc định nếu chưa có
        if 'picking_type_id' not in vals:
            vals['picking_type_id'] = self.env.ref('stock.picking_type_in').id
        
        # Gọi super trước
        picking = super(Inventory, self).create(vals)
        
        # Nếu là loại nhập kho thì chuyển sang "Chờ phê duyệt"
        if picking.picking_type_id.code == 'incoming':
            picking.action_confirm()

        return picking
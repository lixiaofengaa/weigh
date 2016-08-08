# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class nc_order_line(models.Model):
    _name = 'weigh.nc_order.line'
    _inherit = ['mail.thread']

    nc_order_no = fields.Char()#nc订单号
    consignee = fields.Char()#
    consignor = fields.Char()
    place = fields.Char()
    price = fields.Float()
    num = fields.Float()
    order_type = fields.Char()
    nc_maker = fields.Char()
    product_template_id = fields.Many2one('product.template')
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('done', 'Done')],
                             string='Status', index=True, readonly=True, default='draft',
                             track_visibility='onchange', copy=False)
    @api.one
    def name_get(self):
        return self.id, self.nc_order_no

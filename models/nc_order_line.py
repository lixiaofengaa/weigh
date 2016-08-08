# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _

class nc_order_line(models.Model):
    _name = 'weigh.nc_order.line'
    _inherit = ['mail.thread']

    nc_order_no = fields.Char()#nc订单号
    consignee = fields.Char()#收货人
    consignor = fields.Char()#发货人
    place = fields.Char()#地点
    price = fields.Float()#金额
    num = fields.Float()#数量
    order_type = fields.Char()#订单类型
    nc_maker = fields.Char()#制单人
    product_template_id = fields.Many2one('product.template')#模板
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('done', 'Done')],
                             string='Status', index=True, readonly=True, default='draft',
                             track_visibility='onchange', copy=False)#状态
    @api.one
    def name_get(self):
        return self.id, self.nc_order_no

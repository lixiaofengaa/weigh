# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class dispatche_vehicle_line(models.Model):
    _name = 'weigh.dispatche_vehicle'
    _inherit = ['mail.thread']

    no = fields.Char()#派车单号
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('done', 'Done')],
                             string='Status', index=True, readonly=True, default='draft',
                             track_visibility='onchange', copy=False)#状态
    nc_order_line_ids = fields.Many2many('weigh.nc_order.line')#NC订单号
    fleet_vehicle_ids = fields.Many2one('fleet.vehicle')#车队号

    estimate_vehicle_entry = fields.Datetime()#估计车辆进入时间

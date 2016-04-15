# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class dispatche_vehicle_line(models.Model):
    _name = 'weigh.dispatche_vehicle'
    _inherit = ['mail.thread']

    no = fields.Char()
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('done', 'Done')],
                             string='Status', index=True, readonly=True, default='draft',
                             track_visibility='onchange', copy=False)
    nc_order_line_ids = fields.Many2many('weigh.nc_order.line')
    fleet_vehicle_ids = fields.Many2one('fleet.vehicle')

    estimate_vehicle_entry = fields.Datetime()

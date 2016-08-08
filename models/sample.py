# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class sample(models.Model):
    _name = 'weigh.sample'          #化验取样
    _inherit = ['mail.thread']

    no = fields.Char()              #编码
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('done', 'Done')],
                             string='Status', index=True, readonly=True, default='draft',
                             track_visibility='onchange', copy=False)#状态
    dispatche_vehicle_id = fields.Many2one('weigh.dispatche_vehicle')#派车单号
    sampler_id = fields.Many2one('res.partner')#取样单号

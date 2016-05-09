# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class sample(models.Model):
    _name = 'weigh.sample'
    _inherit = ['mail.thread']

    no = fields.Char()
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('done', 'Done')],
                             string='Status', index=True, readonly=True, default='draft',
                             track_visibility='onchange', copy=False)
    dispatche_vehicle_id = fields.Many2one('weigh.dispatche_vehicle')
    sampler_id = fields.Many2one('res.partner')

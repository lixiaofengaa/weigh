# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class fleet_vehicle(models.Model):
    _name = 'fleet.vehicle'
    _inherit = ['fleet.vehicle']

    tare = fields.Float()#皮重
    owner_id = fields.Many2one('res.partner')#车队所有人

# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class confirm_goods(models.Model):
    _name = 'weigh.confirm_goods'
    _inherit = ['mail.thread']

    dispatche_vehicle_id = fields.Many2one('weigh.dispatche_vehicle')

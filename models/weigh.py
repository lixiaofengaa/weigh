# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class weigh(models.Model):
    _name = 'weigh.weigh'#重量
    _inherit = ['mail.thread']

    dispatche_vehicle_id = fields.Many2one('weigh.dispatche_vehicle')#派车单号

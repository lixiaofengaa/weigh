# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class vehicle_queue(models.Model):
    _name = 'weigh.vehicle_queue'
    _inherit = ['mail.thread']

    dispatche_vehicle_id = fields.Many2one('weigh.dispatche_vehicle')
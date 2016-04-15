# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class pass_gate(models.Model):
    _name = 'weigh.pass_gate'
    _inherit = ['mail.thread']

    dispatche_vehicle_id = fields.Many2one('weigh.dispatche_vehicle')
    gates_id = fields.Many2one('weigh.gates')
    is_in = fields.Boolean()

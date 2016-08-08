# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class pass_gate(models.Model):
   _name = 'weigh.pass_gate'#通过门岗
    _inherit = ['mail.thread']

    dispatche_vehicle_id = fields.Many2one('weigh.dispatche_vehicle')#派车单号
    gates_id = fields.Many2one('weigh.gates')#门岗ID
    in_out = fields.Selection([('in', 'in'),
                               ('out', 'out')])#进/出门岗

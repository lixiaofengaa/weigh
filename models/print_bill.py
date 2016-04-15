# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class print_bill(models.Model):
    _name = 'weigh.print_bill'
    _inherit = ['mail.thread']

    dispatche_vehicle_id = fields.Many2one('weigh.dispatche_vehicle')

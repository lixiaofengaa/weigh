# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class vehicle_code(models.Model):
    _name = 'weigh.vehicle_code'
    _inherit = ['mail.thread']

    code = fields.Char()

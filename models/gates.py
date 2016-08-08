# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class gates(models.Model):
    _name = 'weigh.gates'
    _inherit = ['mail.thread']

    name = fields.Char()#门岗

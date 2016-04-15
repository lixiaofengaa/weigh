# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class parameter(models.Model):
    _name = 'weigh.parameter'
    _inherit = ['mail.thread']

    template_ids = fields.Many2many('product.template')

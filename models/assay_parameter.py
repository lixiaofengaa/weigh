# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class assay_parameter(models.Model):
    _name = 'weigh.assay_parameter'
    _inherit = ['mail.thread']

    assay_id = fields.Many2one('weigh.assay')
    parameter_id = fields.Many2one('weigh.parameter')
    value = fields.Float()

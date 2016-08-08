# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class assay(models.Model):
    _name = 'weigh.assay'#化验
    _inherit = ['mail.thread']

    sample_id = fields.Many2one('weigh.sample')#取样单号
    assay_parameter_ids = fields.One2many('weigh.assay_parameter', 'assay_id')#化验单号

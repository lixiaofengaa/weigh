# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import osv
from openerp.tools.translate import _


class assay(models.Model):
    _name = 'weigh.assay'
    _inherit = ['mail.thread']

    sample_id = fields.Many2one('tender.sample')

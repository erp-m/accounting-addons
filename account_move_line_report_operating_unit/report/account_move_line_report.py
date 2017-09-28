# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import tools, models, fields, api
import openerp.addons.decimal_precision as dp

class AccountMoveLineReport(models.Model):
    _inherit = "account.move.line.report"

    operating_unit_id = fields.Many2one(
        comodel_name='operating.unit',
        string='Operating Unit', readonly=True)

    def _select(self):
        return super(AccountMoveLineReport, self)._select(
        ) + " , aml.operating_unit_id as operating_unit_id"
# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import tools, models, fields, api
import openerp.addons.decimal_precision as dp

class AccountMoveLineReport(models.Model):
    _inherit = "account.move.line.report"

    product_maincategory = fields.Many2one(
        comodel_name='product.category',
        string='Top Level Category', readonly=True)

    def _select(self):
        return super(AccountMoveLineReport, self)._select(
        ) + " , pp.main_category as product_maincategory"


    def _from(self):
        return super(AccountMoveLineReport, self)._from(
        ) + " LEFT JOIN product_product pp on aml.product_id=pp.id"
# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields


class AccountStatementOperationTemplate(models.Model):
    _inherit = 'account.statement.operation.template'

    analytic_dimension_policy = fields.Selection(
            string='Policy for analytic dimension',
            related='account_id.analytic_dimension_policy', readonly=True)

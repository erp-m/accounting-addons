# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields


class AccountStatementOperationTemplate(models.Model):
    _inherit = 'account.statement.operation.template'

    costcenter_policy = fields.Selection(
        string='Policy for costcenter dimension',
        related='account_id.costcenter_policy', readonly=True)
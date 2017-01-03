# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields, api, _


class AccountAccount(models.Model):
    _inherit = "account.account"

    @api.model
    def _get_policies(self):
        return self.env['account.account.type']._get_policies()

    analytic_policy = fields.Selection(
            seelction='_get_policies',
            string='Policy for analytic dimension'
    )

    analytic_dimension_policy = fields.Selection(
        compute='_get_analytic_dimension_policy',
        store=True,
        related='',
    )

    @api.depends('user_type', 'analytic_policy')
    @api.one
    def _get_analytic_dimension_policy(self):
        if self.analytic_policy:
            self.analytic_dimension_policy = self.analytic_policy
        elif self.user_type and self.user_type.analytic_dimension_policy:
            self.analytic_dimension_policy = self.user_type.analytic_dimension_policy
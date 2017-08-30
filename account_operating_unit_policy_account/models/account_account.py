# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields, api, _


class AccountAccount(models.Model):
    _inherit = "account.account"

    @api.model
    def _get_policies(self):
        return self.env['account.account.type']._get_policies()

    operating_unit_account_policy = fields.Selection(
            selection='_get_policies',
            string='Policy for cost center dimension'
    )

    operating_unit_policy = fields.Selection(
            selection='_get_policies',
            compute='_get_operating_unit_policy',
            store=True,
            related='',
    )

    @api.depends('user_type.operating_unit_policy', 'operating_unit_account_policy')
    @api.one
    def _get_operating_unit_policy(self):
        if self.operating_unit_account_policy:
            self.operating_unit_policy = self.operating_unit_account_policy
        elif self.user_type and self.user_type.operating_unit_policy:
            self.operating_unit_policy = self.user_type.operating_unit_policy

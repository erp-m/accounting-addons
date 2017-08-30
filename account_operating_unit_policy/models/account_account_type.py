# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields, api, _


class AccountAccountType(models.Model):
    _inherit = 'account.account.type'

    operating_unit_policy = fields.Selection(
        '_get_policies', string='Operating Unit Policy',
        required=True, default=lambda self: self._default_policy())


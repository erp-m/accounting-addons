# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields


class AccountAccount(models.Model):
    _inherit = "account.account"

    operating_unit_policy = fields.Selection(
            string='Operating Unit Policy',
            related='user_type.operating_unit_policy', readonly=True)

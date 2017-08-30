# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    operating_unit_policy = fields.Selection(
        string='Operating Unit Policy',
        related='account_id.operating_unit_policy', readonly=True)

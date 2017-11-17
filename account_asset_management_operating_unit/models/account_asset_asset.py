# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)


class AccountAssetAsset(models.Model):
    _inherit = 'account.asset.asset'

    operating_unit_id = fields.Many2one(
        comodel_name='operating.unit',
        string='Operating Unit',
        readonly=True,
        states={'draft': [('readonly', False)]}
    )

    @api.multi
    @api.onchange('operating_unit_id')
    def _get_analytic_account_id(self):
        for rec in self:
            if rec.operating_unit_id and rec.operating_unit_id.analytic_account:
                rec.account_analytic_id = rec.operating_unit_id.analytic_account.id

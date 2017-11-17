# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)


class AccountAssetRemove(models.TransientModel):
    _inherit = 'account.asset.remove'

    @api.model
    def _get_removal_data(self, wiz_data, asset, residual_value):
        move_lines = super(AccountAssetRemove, self)._get_removal_data(
            wiz_data, asset, residual_value
        )
        new_move_lines = []
        for move_line in move_lines:
            new_vals = move_line[2] or {}
            _logger.debug("MoveLine: %s", new_vals)
            if asset.operating_unit_id:
                new_vals.update({'operating_unit_id': asset.operating_unit_id.id})
            new_move_lines.append((0, 0, new_vals))

        return new_move_lines

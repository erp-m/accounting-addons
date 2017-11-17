# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)


class AccountAssetDepreciationLine(models.Model):
    _inherit = 'account.asset.depreciation.line'


    def _setup_move_data(self, depreciation_line, depreciation_date,
                         period_id, context):
        move_data = super(AccountAssetDepreciationLine, self)._setup_move_data(
            depreciation_line, depreciation_date, period_id, context
        )
        asset = depreciation_line.asset_id
        if asset.operating_unit_id:
            move_data.update(
                {'operating_unit_id': asset.operating_unit_id.id})
        _logger.debug("MoveData: %s", move_data)
        return move_data

    def _setup_move_line_data(self, depreciation_line, depreciation_date,
                              period_id, account_id, type, move_id, context):
        move_line_data = super(AccountAssetDepreciationLine, self)._setup_move_line_data(
            depreciation_line, depreciation_date, period_id, account_id, type, move_id, context
        )
        asset = depreciation_line.asset_id
        if asset.operating_unit_id:
            move_line_data.update({'operating_unit_id': asset.operating_unit_id.id})
        _logger.debug("MoveLineData: %s", move_line_data)
        return move_line_data
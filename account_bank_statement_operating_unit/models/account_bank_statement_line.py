# -*- coding: utf-8 -*-
# Copyright (c) 2009-2016 Noviat nv/sa (www.noviat.com)
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import api, fields, models


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    @api.model
    def _default_operating_unit(self):
        return self.env['operating.unit'].browse(
                self._context.get('operating_unit_id', None))

    operating_unit_id = fields.Many2one(
            comodel_name='operating.unit',
            string='Operating Unit',
            default=_default_operating_unit
    )

    @api.model
    def get_statement_line_for_reconciliation(self, st_line):
        data = super(AccountBankStatementLine, self).\
            get_statement_line_for_reconciliation(st_line)
        data['operating_unit_id'] = st_line.operating_unit_id.id
        return data

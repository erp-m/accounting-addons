# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import logging
from openerp import models, fields, api, _

_logger = logging.getLogger(__name__)

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    operating_unit_id = fields.Many2one(
        comodel_name='operating.unit',
        related=False,
        string='Operating Unit',
        readonly=False,
        # default=_default_operating_unit
    )

    @api.model
    def move_line_get_item(self, line):
        res = super(AccountInvoiceLine, self).move_line_get_item(line)
        if line.operating_unit_id:
            res['operating_unit_id'] = line.operating_unit_id.id
        return res

    @api.model
    def _anglo_saxon_sale_move_lines(self, i_line, res):
        """Return the additional move lines for sales invoices and refunds.

        i_line: An account.invoice.line object.
        res: The move line entries produced so far by the parent move_line_get.
        """

        res = super(AccountInvoiceLine, self)._anglo_saxon_sale_move_lines(
            i_line, res
        )
        for moveline in res:
            if moveline.get('invl_id'):
                invoice_line = self.env['account.invoice.line'].search(
                    [
                        ('id', '=', moveline.get('invl_id'))
                    ]
                )
                if invoice_line and invoice_line.operating_unit_id:
                    moveline.update(
                        {'operating_unit_id': invoice_line.operating_unit_id.id}
                    )
        return res
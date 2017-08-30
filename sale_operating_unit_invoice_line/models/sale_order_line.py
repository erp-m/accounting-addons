# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import logging
from openerp import models, fields, api, _

_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.model
    def _prepare_order_line_invoice_line(self, line, account_id=False):
        """Add Operating Unit to each invoice line
        """
        res = super(SaleOrderLine, self)._prepare_order_line_invoice_line(line, account_id=account_id)

        if not line.invoiced and res:
            if line.order_id.operating_unit_id:
                res.update({'operating_unit_id': line.order_id.operating_unit_id.id})

        return res
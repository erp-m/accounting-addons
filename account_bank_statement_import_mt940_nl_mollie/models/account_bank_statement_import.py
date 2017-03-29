# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import logging

from openerp import models
from .mt940 import MT940Parser as Parser


_logger = logging.getLogger(__name__)


class AccountBankStatementImport(models.TransientModel):
    """Add parsing of RABO mt940 files to bank statement import."""
    _inherit = 'account.bank.statement.import'

    def _parse_file(self, cr, uid, data_file, context=None):
        """Parse a MT940 RABO file."""
        parser = Parser()
        try:
            _logger.debug("Try parsing with MT940 Mollie.")
            statements = parser.parse(data_file)
            return statements
        except ValueError:
            # Returning super will call next candidate:
            _logger.debug("Statement file was not a MT940 Mollie file.",
                          exc_info=True)
            return super(AccountBankStatementImport, self)._parse_file(
                cr, uid, data_file, context=context)

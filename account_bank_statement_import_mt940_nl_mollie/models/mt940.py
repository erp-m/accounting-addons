# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
import re
from string import printable
from openerp.addons.account_bank_statement_import_mt940_base.mt940 import (
    MT940, str2amount, get_subfields, handle_common_subfields)


class MT940Parser(MT940):
    """Implement parser for MT940 files - Rabobank dialect."""

    tag_61_regex = re.compile(
        r'^(?P<date>\d{6})(?P<time>\d{4})(?P<sign>[CD])(?P<amount>\d+,\d{2})N(?P<type>.{3})'
    )

    def __init__(self):
        """Initialize parser - override at least header_regex."""
        super(MT940Parser, self).__init__()
        self.mt940_type = 'MOLLIE'
        self.header_lines = 0  # Number of lines to skip
        # Do not user $ for end of string below: line contains much
        # more data than just the first line.
        self.header_regex = '^:20:'  # Start of relevant data

    def parse(self, data):
        """Filter Unprintable characters from file data.

        Remove Any Unprintable Characters
        """
        data = ''.join([x for x in data if x in printable])
        return super(MT940Parser, self).parse(data)

    def handle_tag_61(self, data):
        """Handle tag 61: transaction data."""
        super(MT940Parser, self).handle_tag_61(data)
        parsed_data = self.tag_61_regex.match(data).groupdict()
        self.current_transaction.transferred_amount = (
            str2amount(parsed_data['sign'], parsed_data['amount']))

    def handle_tag_86(self, data):
        """Handle tag 86: transaction details"""
        if not self.current_transaction:
            return
        codewords = ['EREF', 'REMI', 'NAME', 'ADDR']
        subfields = get_subfields(data, codewords)
        transaction = self.current_transaction
        # If we have no subfields, set message to whole of data passed:
        if not subfields:
            transaction.message = data
        else:
            handle_common_subfields(transaction, subfields)
            # Use subfields for transaction details:
            if 'REMI' in subfields:
                transaction.name = ' '.join(subfields['REMI'])
            if 'EREF' in subfields:
                if 'ref'in transaction:
                    transaction['ref'] = ' '.join(subfields['EREF'])
                    if transaction['ref'] == 'NOTPROVIDED':
                        transaction['ref'] = False

        # Prevent handling tag 86 later for non transaction details:
        self.current_transaction = None

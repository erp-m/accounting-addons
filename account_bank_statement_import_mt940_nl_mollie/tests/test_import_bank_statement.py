# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from openerp.addons.account_bank_statement_import.tests import (
    TestStatementFile)


class TestImport(TestStatementFile):
    """Run test to import MT940 RABO import."""

    def setUp(self):
        super(TestImport, self).setUp()
        import_wizard = self.env['account.bank.statement.import']
        import_wizard._create_bank_account(
            'NL34RABO0142623393', company_id=self.env.user.company_id.id)

    def test_statement_import(self):
        """Test correct creation of single statement."""
        transactions = [
            {
                'remote_account': 'NL66RABO0160878799',
                'transferred_amount': 400.00,
                'value_date': '2014-01-02',
                'ref': 'NONREF',
            },
        ]
        # statement name is account number + '-' + date of last 62F line:
        self._test_statement_import(
            'account_bank_statement_import_mt940_nl_rabo', 'test-rabo.swi',
            'NL34RABO0142623393-2014-01-07',
            local_account='NL34RABO0142623393',
            start_balance=4433.52, end_balance=4798.91,
            transactions=transactions
        )

# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Operating Unit Policy',
    'version': '8.0.0.0.5',
    'license': 'AGPL-3',
    'author': 'ICTSTUDIO',
    'category': 'Accounting & Finance',
    'depends': [
        'account_analytic_dimension_policy',
        'account_operating_unit_invoice_line',
        'account_bank_statement_operating_unit'
        ],
    'data': [
        'views/account_account_type.xml',
        'views/account_invoice.xml',
        'views/account_move.xml',
        'views/account_move_line.xml',
        'views/account_statement_operation_template.xml',
        'views/assets_backend.xml',
        ],
    'installable': True,
}

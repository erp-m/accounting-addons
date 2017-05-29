# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Cost Center Policy',
    'version': '8.0.0.0.6',
    'license': 'AGPL-3',
    'author': 'ICTSTUDIO, André Schenkels',
    'category': 'Accounting & Finance',
    'depends': [
        'account_analytic_dimension_policy',
        'account_cost_center'
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

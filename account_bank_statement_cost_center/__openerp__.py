# -*- coding: utf-8 -*-
# Copyright (c) 2009-2016 Noviat nv/sa (www.noviat.com)
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Cost Center on Bank Statement',
    'version': '8.0.1.2.1',
    'license': 'AGPL-3',
    'author': 'ICTSTUDIO',
    'category': 'Accounting & Finance',
    'summary': 'Encode Bank Statements with Cost Centers',
    'depends': ['account_cost_center'],
    'data': [
        'views/account_bank_statement.xml',
        'views/account_statement_operation_template.xml',
        'views/assets_backend.xml',
        ],
    'installable': True,
}

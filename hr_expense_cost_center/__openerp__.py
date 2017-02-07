# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'HR Expense - Cost Center',
    'version': '8.0.0.0.2',
    'license': 'AGPL-3',
    'author': 'ICTSTUDIO',
    'category': 'Accounting & Finance',
    'depends': ['hr_expense',
                'account_cost_center'],
    'data': [
        'views/hr_expense.xml',
        ],
    'installable': True,
}

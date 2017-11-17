# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Management Asset - Operating Unit',
    'version': '8.0.1.0.0',
    'category': 'Reporting',
    'summary': 'Add Operating Unit to Asset Management',
    'author': 'ICTSTUDIO',
    'website': "http://www.ictstudio.eu",
    'license': 'AGPL-3',
    'depends': [
        'account_asset_management',
        'account_operating_unit'
    ],
    'data': [
        'views/account_asset_asset.xml',
    ],
}

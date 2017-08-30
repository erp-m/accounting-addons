# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "MIS Builder Operating Unit Filter",
    'version': '8.0.1.0.0',
    'category': 'Reporting',
    'summary': """
        Add operating unit filters to MIS Reports
    """,
    'author':
        'ICTSTUDIO,'
        'ACSONE SA/NV,'
        'Odoo Community Association (OCA)',
    'website': "http://www.ictstudio.eu",
    'license': 'AGPL-3',
    'depends': [
        'mis_builder',
        'account_operating_unit'
    ],
    'data': [
        'views/mis_report_view.xml',
        'views/mis_builder_operating_unit.xml',
    ],
    'qweb': [
        'static/src/xml/mis_widget.xml'
    ],
}

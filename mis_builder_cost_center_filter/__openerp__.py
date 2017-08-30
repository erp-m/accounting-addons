# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "MIS Builder Cost Center Filter",
    'version': '8.0.1.0.0',
    'category': 'Reporting',
    'summary': """
        Add Cost Center filters to MIS Reports
    """,
    'author':
        'ICTSTUDIO,'
        'ACSONE SA/NV,'
        'Odoo Community Association (OCA)',
    'website': "http://www.ictstudio.eu",
    'license': 'AGPL-3',
    'depends': [
        'mis_builder',
        'account_cost_center'
    ],
    'data': [
        'views/mis_report_view.xml',
        'views/mis_builder_cost_center.xml',
    ],
    'qweb': [
        'static/src/xml/mis_widget.xml'
    ],
}

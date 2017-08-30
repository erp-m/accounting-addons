# -*- coding: utf-8 -*-
# Copyright (c) 2009-2016 Noviat nv/sa (www.noviat.com)
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import api, fields, models


class AccountStatementOperationTemplate(models.Model):
    _inherit = 'account.statement.operation.template'

    operating_unit_id = fields.Many2one(
            comodel_name='operating.unit',
            string='Operating Unit',
            ondelete='set null'
    )
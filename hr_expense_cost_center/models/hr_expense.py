# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields, api, _


class HrExpense(models.Model):
    _inherit = "hr.expense"

    @api.model
    def _default_cost_center(self):
        return self.env['account.cost.center'].browse(
                self._context.get('cost_center_id'))

    cost_center_id = fields.Many2one(
            comodel_name='account.cost.center',
            string='Cost Center',
            default=_default_cost_center
    )

    @api.model
    def move_line_get_item(self, line):
        data = super(HrExpense, self).move_line_get_item(line)

        data['cost_center_id'] = self.cost_center_id and self.cost_center_id.id
        return data
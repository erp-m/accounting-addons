# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class MisReportInstance(models.Model):
    _inherit = 'mis.report.instance'

    cost_center_id = fields.Many2one(
        comodel_name='account.cost.center',
        string='Cost Center'
    )

    @api.multi
    def preview(self):
        self.ensure_one()
        res = super(MisReportInstance, self).preview()
        res['context'] = {
            'cost_center_id': self.cost_center_id.id,
        }
        return res


class MisReportInstancePeriod(models.Model):
    _inherit = 'mis.report.instance.period'

    @api.multi
    def _get_additional_move_line_filter(self):
        self.ensure_one()
        res = super(MisReportInstancePeriod, self).\
            _get_additional_move_line_filter()
        val = self.env.context.get('cost_center_id')
        if val:
            res.append(('cost_center_id', '=', val))
        return res

    @api.multi
    def _get_additional_query_filter(self, query):
        self.ensure_one()
        res = super(MisReportInstancePeriod, self).\
            _get_additional_move_line_filter()
        # TODO filter on cost center if query.model_id has
        #      a field of type cost_center_id
        return res

# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class MisReportInstance(models.Model):
    _inherit = 'mis.report.instance'

    operating_unit_id = fields.Many2one(
        comodel_name='operating.unit', string='Operating Unit')

    @api.multi
    def preview(self):
        self.ensure_one()
        res = super(MisReportInstance, self).preview()
        res['context'] = {
            'operating_unit_id': self.operating_unit_id.id,
        }
        return res


class MisReportInstancePeriod(models.Model):
    _inherit = 'mis.report.instance.period'

    @api.multi
    def _get_additional_move_line_filter(self):
        self.ensure_one()
        res = super(MisReportInstancePeriod, self).\
            _get_additional_move_line_filter()
        val = self.env.context.get('operating_unit_id')
        if val:
            res.append(('operating_unit_id', '=', val))
        return res

    @api.multi
    def _get_additional_query_filter(self, query):
        self.ensure_one()
        res = super(MisReportInstancePeriod, self).\
            _get_additional_move_line_filter()
        # TODO filter on analytic account if query.model_id has
        #      a field of type operating_unit_id
        return res

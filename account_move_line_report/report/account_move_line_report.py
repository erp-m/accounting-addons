# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import tools, models, fields, api
import openerp.addons.decimal_precision as dp

class AccountMoveLineReport(models.Model):
    _name = "account.move.line.report"
    _description = "Journal Items Advanced Analysis"
    _auto = False
    _rec_name = 'date_effective'

    date = fields.Date(string='Effective Date', readonly=True)
    date_effective = fields.Date(string='Effective Date', readonly=True)
    date_created = fields.Date(string='Date Created', readonly=True)
    date_maturity = fields.Date(string='Date Maturity', readonly=True)
    ref = fields.Char(string='Reference', readonly=True)
    nbr = fields.Integer(string='# of Items', readonly=True)
    debit = fields.Float(string='Debit', readonly=True)
    credit = fields.Float(string='Credit', readonly=True)
    balance = fields.Float(string='Balance', readonly=True)
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency', readonly=True)
    amount_currency = fields.Float(
        string='Amount Currency',
        digits_compute=dp.get_precision('Account'), readonly=True)
    period_id = fields.Many2one(
        comodel_name='account.period',
        string='Period', readonly=True)
    account_id = fields.Many2one(
        comodel_name='account.account',
        string='Account', readonly=True)
    journal_id = fields.Many2one(
        comodel_name='account.journal', string='Journal', readonly=True)
    fiscalyear_id = fields.Many2one(
        comodel_name='account.fiscalyear', string='Fiscal Year', readonly=True)
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product', readonly=True)
    product_uom_id = fields.Many2one(
        comodel_name='product.uom',
        string='Product Unit of Measure', readonly=True)
    move_state = fields.Selection(
        selection=[('draft','Unposted'), ('posted','Posted')],
        string='Status', readonly=True)
    move_line_state = fields.Selection(
        selection=[('draft','Unbalanced'), ('valid','Valid')],
        string='State of Move Line', readonly=True)
    reconcile_id = fields.Many2one(
        comodel_name='account.move.reconcile',
        string='Reconciliation number', readonly=True)
    partner_id = fields.Many2one('res.partner','Partner', readonly=True)
    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analytic Account', readonly=True)
    product_quantity = fields.Float(
        string='Products Quantity', digits=(16,2), readonly=True)
    user_type = fields.Many2one(
        comodel_name='account.account.type',
        string='Account Type', readonly=True)
    type = fields.Selection(
        selection=[
            ('receivable', 'Receivable'),
            ('payable', 'Payable'),
            ('cash', 'Cash'),
            ('view', 'View'),
            ('consolidation', 'Consolidation'),
            ('other', 'Regular'),
            ('closed', 'Closed'),
        ],
        string='Internal Type',
        readonly=True,
        help="This type is used to differentiate types with "\
             "special effects in Odoo: view can not have entries, consolidation are accounts that "\
             "can have children accounts for multi-company consolidations, payable/receivable are for "\
             "partners accounts (for debit/credit computations), closed for depreciated accounts.")
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        readonly=True
    )

    _order = 'date_effective desc'

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        fiscalyear_obj = self.env['account.fiscalyear']
        period_obj = self.env['account.period']
        for arg in args:
            if arg[0] == 'period_id' and arg[2] == 'current_period':
                current_period = period_obj.find()[0]
                args.append(['period_id', 'in', [current_period.id]])
                break
            elif arg[0] == 'period_id' and arg[2] == 'current_year':
                current_year = fiscalyear_obj.find()
                ids = fiscalyear_obj.read([current_year.id], ['period_ids'])[0]['period_ids']
                args.append(['period_id', 'in', ids])
        for a in [['period_id', 'in', 'current_year'], ['period_id', 'in', 'current_period']]:
            if a in args:
                args.remove(a)
        return super(AccountMoveLineReport, self).search(
            args=args, offset=offset, limit=limit, order=order, count=count)

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False,lazy=True):
        fiscalyear_obj = self.env['account.fiscalyear']
        period_obj = self.env['account.period']
        if self._context.get('period', False) == 'current_period':
            current_period = period_obj.find()[0]
            domain.append(['period_id', 'in', [current_period.id]])
        elif self._context.get('year', False) == 'current_year':
            current_year = fiscalyear_obj.find()
            ids = fiscalyear_obj.read([current_year.id], ['period_ids'])[0]['period_ids']
            domain.append(['period_id', 'in', ids])
        else:
            domain = domain
        return super(AccountMoveLineReport, self).read_group(
            domain, fields, groupby, offset=offset, limit=limit,
            orderby=orderby, lazy=lazy)


    def _select(self):
        select_str = """
            SELECT
                aml.id as id,
                am.date as date_effective,
                aml.date_maturity as date_maturity,
                aml.date_created as date_created,
                am.ref as ref,
                am.state as move_state,
                aml.state as move_line_state,
                aml.reconcile_id as reconcile_id,
                aml.partner_id as partner_id,
                aml.product_id as product_id,
                aml.product_uom_id as product_uom_id,
                am.company_id as company_id,
                am.journal_id as journal_id,
                ap.fiscalyear_id as fiscalyear_id,
                am.period_id as period_id,
                aml.account_id as account_id,
                aml.analytic_account_id as analytic_account_id,
                aa.type as type,
                aa.user_type as user_type,
                1 as nbr,
                aml.quantity as quantity,
                aml.currency_id as currency_id,
                aml.amount_currency as amount_currency,
                aml.debit as debit,
                aml.credit as credit,
                coalesce(aml.debit, 0.0) - coalesce(aml.credit, 0.0) as balance
        """
        return select_str


    def _from(self):
        from_str = """
                FROM account_move_line aml
                LEFT JOIN account_account aa on (aml.account_id = aa.id)
                LEFT JOIN account_move am on (am.id=aml.move_id)
                LEFT JOIN account_period ap on (am.period_id=ap.id)"""
        return from_str

    def _where(self):
        where_str = """
                WHERE aml.state != 'draft'"""
        return where_str


    def _group_by(self):
        group_by_str = """
        """
        return group_by_str

    def init(self, cr):
        """Initialize the sql view for the event registration """
        tools.drop_view_if_exists(cr, self._table)

        cr.execute("""CREATE VIEW %s AS ( %s
            %s
            %s
            %s
            )""" %
                   (
                       self._table,
                       self._select(),
                       self._from(),
                       self._where(),
                       self._group_by()
                   )
                   )
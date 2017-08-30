/*
 * Copyright © 2016 ICTSTUDIO <http://www.ictstudio.eu>
 * License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
 */

openerp.account_bank_statement_operating_unit = function (instance) {
    var _t = instance.web._t;
    var QWeb = instance.web.qweb;

    instance.web.account.bankStatementReconciliation.include({

        init: function(parent, context) {
            this._super.apply(this, arguments);

            this.create_form_fields['operating_unit_id'] = {
                id: "operating_unit_id",
                index: 5,
                label: _t("Operating Unit"),
                corresponding_property: "operating_unit_id",
                tabindex: 15,
                constructor: instance.web.form.FieldMany2One,
                field_properties: {
                    relation: "operating.unit",
                    string: _t("Operating Unit"),
                    type: "many2one",
                },
            };

        },

        start: function() {
            this._super();
            var self = this;
            // Retreive statement infos and reconciliation data from the model
            var lines_filter = [['journal_entry_id', '=', false], ['account_id', '=', false]];
            var deferred_promises = [];

            // Get operation templates
            deferred_promises.push(new instance.web.Model("account.statement.operation.template")
                .query(['id','name','account_id','label','amount_type','amount','tax_id','analytic_account_id','operating_unit_id'])
                .all().then(function (data) {
                    _(data).each(function(preset){
                        self.presets[preset.id] = preset;
                    });
                })
            );
        },

    });

    instance.web.account.bankStatementReconciliationLine.include({

        initializeCreateForm: function() {
            this._super.apply(this, arguments);
            var self = this;
            self.operating_unit_id_field.set("value", self.st_line.operating_unit_id)
        },

        prepareCreatedMoveLineForPersisting: function(line) {
            var dict = this._super.apply(this, arguments);
            var self = this;
            if (line.operating_unit_id) dict['operating_unit_id'] = line.operating_unit_id;
            return dict;
        },

    });

};
/*
 # Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
 # License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
*/
openerp.account_analytic_dimension_policy_views = function (instance) {
    var _t = instance.web._t;
    var QWeb = instance.web.qweb;

    instance.web.account.bankStatementReconciliationLine.include({

        init: function(parent, context) {
            this._super.apply(this, arguments);
            this.map_analytic_dimension_policy = this.getParent().map_analytic_dimension_policy;
            this.required_fields_set = this.getParent().required_fields_set;
            },

        UpdateRequiredFields: function(elt) {
            if (elt.get('value')) {
                this.required_fields_set[elt.name] = true;
            } else {
                this.required_fields_set[elt.name] = false;
            };
            var balanceChangedFlag = this.CheckRequiredFields(elt);
            if (balanceChangedFlag) {
                this.balanceChanged();      
            } else {
                this.$(".button_ok").text("OK").removeClass("oe_highlight").attr("disabled", "disabled");
            };
        },

        CheckRequiredFields: function() {
            var flag = _.every(this.required_fields_set);
            return flag;
        },

        formCreateInputChanged: function(elt, val) {
            this._super.apply(this, arguments);
            if (elt === this.account_id_field) {
                if (this.map_analytic_dimension_policy[elt.get('value')] === 'always') {
                    this.analytic_account_id_field.modifiers = {'required': true, 'readonly': false};
                    this.required_fields_set['cost_center_id'] = false;
                    if (! this.analytic_account_id_field.get('value')) {
                        this.$(".button_ok").text("OK").removeClass("oe_highlight").attr("disabled", "disabled");
                    };
                } else {
                    delete this.required_fields_set['analytic_account_id'];
                    if (this.map_analytic_dimension_policy[elt.get('value')] === 'never') {
                        this.analytic_account_id_field.set('value', false);
                        this.analytic_account_id_field.modifiers = {'required': false, 'readonly': true};
                    } else {
                        this.analytic_account_id_field.modifiers = {'required': false, 'readonly': false};
                    };
                };
                this.analytic_account_id_field.field_manager.do_show();
            };
            if (elt.name === 'analytic_account_id') {
                if ('analytic_account_id' in this.required_fields_set)  {
                    this.UpdateRequiredFields(elt);
                };
            };
        },

    });

};

/*
 * Copyright © 2017 ICTSTUDIO <http://www.ictstudio.eu>
 * License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
 */
openerp.account_operating_unit_policy = function (instance) {
    var _t = instance.web._t;
    var QWeb = instance.web.qweb;

    instance.web.account.bankStatementReconciliation.include({

        init: function(parent, context) {
            this._super.apply(this, arguments);
            this.model_account = new instance.web.Model("account.account");
            this.map_operating_unit_policy = {};
            var required_dict = {};
            _.each(this.create_form_fields, function(field) {                
                if (field['required']) {
                    required_dict[field['id']] = false;
                    };
                });
            /* 
            this.required_fields_set is used to check if all required fields 
            are filled in before showing the 'Ok' button on a line
            */
            this.required_fields_set = required_dict;
        },

        start: function() {
            var tmp = this._super.apply(this, arguments);
            var self = this;
            maps = [];
            maps.push(this.model_account
                .query(['id', 'operating_unit_policy'])
                .filter([['type', 'not in', ['view', 'consolidation', 'closed']]])
                .all().then(function(data) {
                    _.each(data, function(o) {
                        self.map_operating_unit_policy[o.id] = o.operating_unit_policy;
                        });
                })
            );
            return $.when(tmp, maps);
        },

    });

    instance.web.account.bankStatementReconciliationLine.include({

        init: function(parent, context) {
            this._super.apply(this, arguments);
            this.map_operating_unit_policy = this.getParent().map_operating_unit_policy;
            this.required_fields_set = this.getParent().required_fields_set;
        },

        formCreateInputChanged: function(elt, val) {
            this._super.apply(this, arguments);
            if (elt === this.account_id_field) {
                this.required_fields_set['operating_unit_id'] = false;
                if (this.map_operating_unit_policy[elt.get('value')] === 'always') {
                    this.operating_unit_id_field.modifiers = {'required': true, 'readonly': false};
                } else {
                    delete this.required_fields_set['operating_unit_id'];
                    if (this.map_operating_unit_policy[elt.get('value')] === 'never') {
                        this.operating_unit_id_field.set('value', false);
                        this.operating_unit_id_field.modifiers = {'required': false, 'readonly': true};
                    } else {
                        this.operating_unit_id_field.modifiers = {'required': false, 'readonly': false};
                    };
                };
                this.operating_unit_id_field.field_manager.do_show();
            };
            if (elt.name in this.required_fields_set) {
                this.UpdateRequiredFields(elt);
            };
            if (this.operating_unit_id_field.get('value')) {
                this.UpdateRequiredFields(this.operating_unit_id_field)
            };

        },

        presetClickHandler: function(e) {
            this._super.apply(this, arguments);
            if (this.operating_unit_id_field.get('value')) {
                this.UpdateRequiredFields(this.operating_unit_id_field)
            };
        },

    });

};

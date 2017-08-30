/* © 2016 ICTSTUDIO
 * © 2016 ACSONE SA/NV
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). 
 */

openerp.mis_builder_operating_unit_filter = function(instance) {
    var _t = instance.web._t;

    instance.mis_builder.MisReport.include({

        init: function() {
            this._super.apply(this, arguments);
            this.operating_unit_id = false;
            this.initialized = false;
            this.mis_report_instance_id = false;
        },
        initialize_field: function() {
            var self = this;
            self.destroy_content();
            self.init_fields();
        },
        destroy_content: function() {
            if (this.dfm) {
                this.dfm.destroy();
                this.dfm = undefined;
            }
        },
        get_context: function() {
            var self = this;
            context = this._super.apply(this, arguments);
            context['operating_unit_id'] = this.operating_unit_id;
            return context
        },
        init_fields: function() {
            var self = this;
            if (self.dfm)
                return;
            var Users = new instance.web.Model('res.users');
            Users.call('has_group', ['operating_unit.group_multi_operating_unit']).done(function (res) {
                if (res) {
                    self.$(".oe_mis_builder_operating_unit_axis").css('visibility', 'visible');
                }
            });
            self.dfm = new instance.web.form.DefaultFieldManager(self);
            self.dfm.extend_field_desc({
                account: {
                    relation: "operating.unit",
                },
            });
            self.account_m2o = new instance.web.form.FieldMany2One(self.dfm, {
                attrs: {
                    placeholder: _t("Operating Unit"),
                    name: "account",
                    type: "many2one",
                    domain: [],
                    context: {},
                    modifiers: '{}',
                },
            });
            if (this.initialized) {
                self.account_m2o.set('value', this.operating_unit_id);
            } else {
                val = self.getParent().dataset.context.operating_unit_id
                if (val) {
                    self.account_m2o.set('value', val);
                    this.operating_unit_id = val
                }
                this.initialized = true;
            }
            self.account_m2o.prependTo(self.$(".oe_mis_builder_operating_unit_axis"));
            self.account_m2o.$input.focusout(function(){
                self.operating_unit_id = self.account_m2o.get_value();
            });
            self.$(".oe_mis_builder_generate_content").click(_.bind(this.generate_content, this));
        },
        renderElement: function() {
            this._super();
            var self = this;
            self.initialize_field();
        },

});
}

/* © 2016 ICTSTUDIO
 * © 2016 ACSONE SA/NV
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). 
 */

openerp.mis_builder_cost_center_filter = function(instance) {
    var _t = instance.web._t;

    instance.mis_builder.MisReport.include({

        init: function() {
            this._super.apply(this, arguments);
            this.cost_center_id = false;
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
            context['cost_center_id'] = this.cost_center_id;
            return context
        },
        init_fields: function() {
            var self = this;
            if (self.dfm)
                return;
            self.dfm = new instance.web.form.DefaultFieldManager(self);
            self.dfm.extend_field_desc({
                account: {
                    relation: "account.cost.center",
                },
            });
            self.account_m2o = new instance.web.form.FieldMany2One(self.dfm, {
                attrs: {
                    placeholder: _t("Cost Center"),
                    name: "account",
                    type: "many2one",
                    domain: [],
                    context: {},
                    modifiers: '{}',
                },
            });
            if (this.initialized) {
                self.account_m2o.set('value', this.cost_center_id);
            } else {
                val = self.getParent().dataset.context.cost_center_id
                if (val) {
                    self.account_m2o.set('value', val);
                    this.cost_center_id = val
                }
                this.initialized = true;
            }
            self.account_m2o.prependTo(self.$(".oe_mis_builder_cost_center_axis"));
            self.account_m2o.$input.focusout(function(){
                self.cost_center_id = self.account_m2o.get_value();
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

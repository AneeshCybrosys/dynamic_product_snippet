odoo.define('dynamic_product_snippet.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet',
       start: function () {
           var self = this;
           console.log("yayay",this)
           rpc.query({
               route: '/total_product_sold',
               params: {},
           }).then(function (result) {
                self.$target.empty().append(result);
           });
       },
   });
   PublicWidget.registry.snippet =  Dynamic;
   console.log('end')
   return Dynamic;
});

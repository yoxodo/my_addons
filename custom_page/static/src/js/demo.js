odoo.define('custom_page.demo', function (require) {
"use strict";

var Widget = require('web.Widget');
var core = require('web.core');

var CustomPageDemo = Widget.extend({
    template: 'DemoPage',
    events: { 'click .demo-submit': '_onSubmitClick' },

    _onSubmitClick: function (e) {
        e.stopPropagation();
        alert('Submit clicked!');
    }
});

core.action_registry.add('custom_page.demo', CustomPageDemo);

return CustomPageDemo;

});

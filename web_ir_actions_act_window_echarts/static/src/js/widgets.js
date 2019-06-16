odoo.define("web.echarts_widgets", function (require) {
    "use strict";

    var core = require("web.core");
    var Widget = require("web.Widget");

    var EchartItem1 = Widget.extend({
        template: "echartItem",
        init: function (parent, action, options) {
            this._super.apply(this, arguments);
            this.data1 = action;
        },
        start: function () {
            var self = this;
            var dom = self.$el.get(0);
            var myChart = echarts.init(dom);

            var option = {
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    data: [820, 932, 901, 934, 1290, 1330, 1320],
                    type: 'line',
                    areaStyle: {}
                }]
            };

            myChart.setOption(option);
            return this._super.apply(this, arguments);
        }
    });

    var EchartItem2 = Widget.extend({
        template: "echartItem",
        init: function (parent, action, options) {
            this._super.apply(this, arguments);
            this.data1 = action;
        },
        start: function () {
            var self = this;
            var dom = self.$el.get(0);
            var myChart = echarts.init(dom);

            var option = {
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)"
                },
                legend: {
                    orient: 'vertical',
                    x: 'left',
                    data: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎']
                },
                series: [
                    {
                        name: '访问来源',
                        type: 'pie',
                        radius: ['50%', '70%'],
                        avoidLabelOverlap: false,
                        label: {
                            normal: {
                                show: false,
                                position: 'center'
                            },
                            emphasis: {
                                show: true,
                                textStyle: {
                                    fontSize: '30',
                                    fontWeight: 'bold'
                                }
                            }
                        },
                        labelLine: {
                            normal: {
                                show: false
                            }
                        },
                        data: [
                            {value: 335, name: '直接访问'},
                            {value: 310, name: '邮件营销'},
                            {value: 234, name: '联盟广告'},
                            {value: 135, name: '视频广告'},
                            {value: 1548, name: '搜索引擎'}
                        ]
                    }
                ]
            };

            myChart.setOption(option);
            return this._super.apply(this, arguments);
        }
    });

    var EchartsAction = Widget.extend({
        template: "echart_template",

        init: function (parent, action, options) {
            this._super.apply(this, arguments);
            this.data1 = action.params.data1;
            this.data2 = action.params.data2;
        },

        start: function () {
            var self = this;

            var chart1 = new EchartItem1(self, self.data1, null);
            chart1.appendTo(self.$el);

            var chart2 = new EchartItem2(self, self.data2, null);
            chart2.appendTo(self.$el);

            return this._super.apply(this, arguments);
        }
    });

    core.action_registry.add("echart.demo", EchartsAction)
});
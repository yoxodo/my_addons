odoo.define('web.web_ir_actions_act_windowe_echarts', function (require) {
    'use strict';

    var ActionManager = require('web.ActionManager');
    var Dialog = require('web.Dialog');
    var core = require('web.core');

    var Qweb = core.qweb;
    var _t = core._t;

   ActionManager.include({
       ir_actions_act_window_echarts: function (action, options) {

       },
       ir_actions_act_window_sales_report_echarts: function (action, options) {

       },
       ir_actions_act_window_output_report_echarts: function (action, options) {

       },
       ir_actions_act_window_expense_income_echarts: function (action, options) {
            var self = this;
            console.log(action);
            var dialog = new Dialog(
                this,
                _.extend({
                    $content: QWeb.render('Expense_Income_Chart', {
                        data: action.data,
                        help_text: action.help_text,
                        flags: action.flags,
                    }),
                    size: action.size || 'large',
                    title: action.name || _t('销售情况'),
                    buttons: [
                        {
                            text: _t('Close'),
                            close: true
                        }
                    ],
                }, options)
            );

            dialog.opened().then(function () {
                self._rpc({
                    route: '/web/sales_report_chart',
                    params: {
                        data: action.data
                    }
                }).then(function (result) {
                    console.log(result);
                    var myChart = echarts.init(document.getElementById('chart-expense-income-report'));

                    var waterMarkText = 'ECHARTS';
                    var themeJson = result.hes_objs;
                    var canvas = document.createElement('canvas');
                    var ctx = canvas.getContext('2d');
                    canvas.width = canvas.height = 100;
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    ctx.globalAlpha = 0.08;
                    ctx.font = '20px Microsoft Yahei';
                    ctx.translate(50, 50);
                    ctx.rotate(-Math.PI / 4);
                    ctx.fillText(waterMarkText, 0, 0);
                    if (result.total_amount) {
                        var option = {
                        backgroundColor: {
                            type: 'pattern',
                            image: canvas,
                            repeat: 'repeat'
                        },
                        tooltip: {},
                        title: [{
                            text: result.title,
                            subtext: '总计： ' + result.sum_sales,
                            x: '25%',
                            textAlign: 'center'
                        },
                            {
                            text: '类型占比',
                            x: '75%',
                            textAlign: 'center'
                        }],
                        grid: [{
                            top: 100,
                            width: '70%',
                            bottom: '5%',
                            height: '80%',
                            left: 10,
                            containLabel: true
                        },],
                        xAxis: [{
                            type: 'category',
                            data: result.expense_name,
                            axisLabel: {
                                interval: 0,
                            },
                            splitLine: {
                                show: false
                            }
                        },],
                        yAxis: [{
                            type: 'value',
                            splitLine: {
                                show: false
                            },
                            axisLabel: {
                                interval: 0,
                                rotate: 30,
                                formatter: '{value} 元'
                            },
                        },],
                        series: [{
                            type: 'bar',
                            stack: 'chart',
                            z: 3,
                            label: {
                                normal: {
                                    position: 'top',
                                    show: true
                                }
                            },
                             itemStyle: {
                                        normal: {
                                            color: '#55A9AF'
                                        }
                                    },
                            data: result.total_amount
                        }, {
                            type: 'pie',
                            radius: [0, '30%'],
                            center: ['75%', '30%'],
                            data: Object.keys(themeJson).map(function (key) {
                                return {
                                    name: key.replace('.js', ''),
                                    value: themeJson[key]
                                }
                            }),
                            itemStyle: {
                                emphasis: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }]
                    };
                    }
                    else {
                        var option = {
                            title: {
                                text: "无数据！",
                            },
                        }
                    }
                    myChart.setOption(option);
                }).fail(function (error, event) {
                    event.preventDefault();
                }).always(function () {
                });
            });
            return dialog.open();
        },
   });
});
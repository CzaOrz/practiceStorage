$(function(){
    // public func for alert
    var
        prompt = function (message, style, time){
            style = (style === undefined) ? 'alert-success' : style;
            time = (time === undefined) ? 1200 : time;
            div = $('<div>')
                .appendTo('body')
                .addClass('alert_window ' + style);
            var _this = div;  // Copy element
            _this.html(message).show(100).delay(time);
            _this.fadeOut("normal", () => _this.remove());
        },
        success_prompt = function(message, time){
            prompt(message, 'alert-success', time);  // Using Bootstrap Style
        },
        danger_prompt = function(message, time){
            prompt(message, 'alert-danger', time);
        };
    // api func
    var
        api_data_for_ziru = () => axios.get('/crawler/api/ziru/data'),
        api_data_for_lagou = () => axios.get('/crawler/api/lagou/data');
    // first tab panel
    new Vue({
        el: '#page-1',
        delimiters: ['[[', ']]'],
        data(){
            return {
                api_ziru_data: null,
            }
        },
        mounted(){
            this.lineChart = echarts.init(document.getElementById('page1-line-chat'));
            this.lineChart.showLoading();
			this.init_api();
        },
        methods: {
            init_api: function(){
                axios.all([api_data_for_ziru(), api_data_for_lagou()])
                .then(axios.spread((ziru, lagou) => {
                    api_result = {
                        'ziru': ziru.data.data.ziru,
                        'lagou': lagou.data.data.lagou,
                    };
                    this.init_line_chart(this.lineChart, api_result);
                }));
            },
            init_line_chart: function(myChart, api_result){
                ziru = api_result.ziru;
                ziru_data_x = [];
                ziru_data_y = [];
                ziru.forEach((e, i, a) => {
                    if (i) {
                        date = new Date(e.timestamp * 1000);
                        ziru_data_x.push(date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate())
                        ziru_data_y.push(a[i].all_count - a[i-1].all_count);
                    }
                })
                option = {
                    title: {
                        text: '爬虫'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data:['自如','拉钩']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: ziru_data_x
                    },
                    yAxis: {
                        type: 'value'
                    },
                    dataZoom: [
                        {
                            show: true,
                            realtime: true,
                            start: 0,
                            end: 100,
                        },
                        {
                            type: 'inside',
                            realtime: true,
                            start: 0,
                            end: 100,
                        }
                    ],
                    series: [
                        {
                            name:'自如-房源增量',
                            type:'line',
                            data: ziru_data_y
                        },
                        {
                            name:'拉钩-python岗',
                            type:'line',
                            data:[220, 182, 191, 234, 290, 330, 310]
                        }
                    ]
                };
                myChart.hideLoading();
				myChart.setOption(option);
            },
        },
    })
})
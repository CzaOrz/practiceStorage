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
    // map for scatter chart
    var
        geoCoordMap = {
            '东莞':[113.75,23.04],
            '天津':[117.2,39.13],
            '长沙':[113,28.21],
            '西安':[108.95,34.27],
            '南京':[118.78,32.04],
            '成都':[104.06,30.67],
            '武汉':[114.31,30.52],
            '杭州':[120.19,30.26],
            '深圳':[114.07,22.62],
            '广州':[113.23,23.16],
            '上海':[121.48,31.22],
            '北京':[116.46,39.92],
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
            this.scatterChinaChart = echarts.init(document.getElementById('page1-scatter-chat'));
            this.lineChart.showLoading();
            this.scatterChinaChart.showLoading();
			this.init_api();
        },
        methods: {
            init_api: function(){
                axios.all([api_data_for_ziru(), api_data_for_lagou()])
                .then(axios.spread((ziru, lagou) => {
                    this.init_line_chart(this.lineChart, ziru.data.data);
                    this.init_scatter_chart(this.scatterChinaChart, lagou.data.data);
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
                        data:['自如']
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
                    ]
                };
                myChart.hideLoading();
				myChart.setOption(option);
            },
            init_scatter_chart: function(myChart, api_result){
                lagou = api_result.lagou;
                res = [];
                normalized_list = [];
                for (key in geoCoordMap) {
                    res.push({
                        name: key,
                        value: geoCoordMap[key].concat(lagou[key]),
                    });
                    normalized_list.push(lagou[key]);
                }
                normalized_list_max = Math.max(...normalized_list);
                normalized_list_min = Math.min(...normalized_list);
                normalized_list_gap = normalized_list_max - normalized_list_min;
                option = {
                    title: {
                        text: '主要城市岗位量 - python',
                        subtext: 'data from lagou',
                        sublink: 'https://www.lagou.com/jobs/allCity.html',
                        left: 'center'
                    },
                    tooltip : {
                        trigger: 'item',
                        formatter: (params) => {
                            if (params.name) {
                                return `<p style="font-size:18px">${params.name}</p>
                                <p style="font-size:14px">python岗位: ${params.value[2]}</p>`;
                            }
                        },
                    },
                    bmap: {
                        center: [104.114129, 37.550339],
                        zoom: 6,
                        roam: true,
                        mapStyle: {
                            styleJson: [{
                                'featureType': 'water',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#d1d1d1'
                                }
                            }, {
                                'featureType': 'land',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#f3f3f3'
                                }
                            }, {
                                'featureType': 'railway',
                                'elementType': 'all',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'highway',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#fdfdfd'
                                }
                            }, {
                                'featureType': 'highway',
                                'elementType': 'labels',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'arterial',
                                'elementType': 'geometry',
                                'stylers': {
                                    'color': '#fefefe'
                                }
                            }, {
                                'featureType': 'arterial',
                                'elementType': 'geometry.fill',
                                'stylers': {
                                    'color': '#fefefe'
                                }
                            }, {
                                'featureType': 'poi',
                                'elementType': 'all',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'green',
                                'elementType': 'all',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'subway',
                                'elementType': 'all',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'manmade',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#d1d1d1'
                                }
                            }, {
                                'featureType': 'local',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#d1d1d1'
                                }
                            }, {
                                'featureType': 'arterial',
                                'elementType': 'labels',
                                'stylers': {
                                    'visibility': 'off'
                                }
                            }, {
                                'featureType': 'boundary',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#fefefe'
                                }
                            }, {
                                'featureType': 'building',
                                'elementType': 'all',
                                'stylers': {
                                    'color': '#d1d1d1'
                                }
                            }, {
                                'featureType': 'label',
                                'elementType': 'labels.text.fill',
                                'stylers': {
                                    'color': '#999999'
                                }
                            }]
                        }
                    },
                    series : [
                        {
                            name: '岗位',
                            type: 'effectScatter',
                            coordinateSystem: 'bmap',
                            data: res,
                            symbolSize: function (val) {
                                return (val[2] - normalized_list_min + 1) * 50 / normalized_list_gap;  // normalized
                            },
                            showEffectOn: 'render',
                            rippleEffect: {
                                brushType: 'stroke'
                            },
                            hoverAnimation: true,
                            label: {
                                normal: {
                                    formatter: '{b}',
                                    position: 'right',
                                    show: true,
                                    textStyle: {
                                        fontSize: 20,
                                    },
                                }
                            },
                            itemStyle: {
                                normal: {
                                    color: 'purple',
                                    shadowBlur: 10,
                                    shadowColor: '#333',
                                }
                            },
                            zlevel: 1
                        }
                    ]
                };
                myChart.hideLoading();
				myChart.setOption(option);
            },
        },
    })
})
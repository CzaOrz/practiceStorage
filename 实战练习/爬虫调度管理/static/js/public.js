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
        api_data_for_ziru = () => axios.get('/crawler/api/ziru/data'),  // for page-1
        api_data_for_lagou = () => axios.get('/crawler/api/lagou/data'),  // for page-1

        api_data_for_news_classify = (data) => axios.post('/other/news/classify', data),  // for page-2

        api_data_for_nodes = () => axios.get('/scheduler/jobs/online/nodes'),  // for page-3
        api_data_for_close_node = (nodeID, pid) => axios.post(`/scheduler/jobs/${nodeID}/${pid}/close`),  // for page-3
        api_data_for_clear_dirty_process = () => axios.post(`/scheduler/jobs/nodes/dirty/process/clear`),  // for page-3

        api_data_for_scheduler_tasks = () => axios.get('/scheduler/jobs'),  // for page-4
        api_data_for_add_task = (data) => axios.post('/scheduler/jobs', data),  // for page-4
        api_data_for_patch_task = (taskID, data) => axios.patch(`/scheduler/jobs/${taskID}`, data),  // for page-4
        api_data_for_deleting_task = (taskID) => axios.delete(`/scheduler/jobs/${taskID}`);  // for page-4

        api_data_for_logs = () => axios.get('/crawler/api/logs'),  // for page-5 logs
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
                        text: '爬虫',
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
                            data: ziru_data_y,
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
                        text: '主要城市岗位分布 - python',
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
                        zoom: 5,
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
    });
    // second tab panel
    new Vue({
        el: '#page-2',
        delimiters: ['[[', ']]'],
        data(){
            return {
                title: '',
                news_classify: [],
                news_classify_running: false,
            }
        },
        methods: {
            init_api: function() {
                this.title = '';
                this.news_classify = [];
                this.news_classify_running = false;
                success_prompt('update successful~', 500);
            },
            classify: function() {
                if (this.news_classify_running) {
                    danger_prompt("this interface is running~ Not try again please~", 1000);
                    return
                }
                if (this.title) {
                    var new_title = this.title;
                    this.news_classify_running = true;
                    api_data_for_news_classify({title: new_title}).then((api_result) => {
                        this.news_classify.push([api_result.data.classify, new_title]);
                        this.news_classify_running = false;
                    }).catch(() => this.news_classify_running = false);
                } else {
                    danger_prompt("Please input an valid title!", 1000);
                }
            },
        },
    });
    // third tab panel
    new Vue({
        el: '#page-3',
        delimiters: ['[[', ']]'],
        data(){
            return {
                nodes: [],
                node_tasks: [],
            }
        },
        mounted(){
            this.init_api();
        },
        methods: {
            init_api: function() {
                api_data_for_nodes().then((api_result) => {
                    this.nodes = api_result.data.nodes;
                    this.node_tasks = api_result.data.tasks;
                })
            },
            close_node: function(task) {
                if (confirm('close this node-process?')){
                    api_data_for_close_node(task[0], task[1].pid).then(() => this.init_api()).catch((e) => {
                        danger_prompt(e, 1000);
                    });
                }
            },
            clear_dirty_process: function() {
                if (confirm('clear the dirty node process?')){
                    api_data_for_clear_dirty_process().then(() => this.init_api()).catch((e) => {
                        danger_prompt(e, 1000);
                    });
                }
            },
        },
    });
    // fourth tab panel
    var page_4 = new Vue({
        el: '#page-4',
        delimiters: ['[[', ']]'],
        data(){
            return {
                scheduler_tasks: null,
            }
        },
        mounted(){
            this.init_api();
        },
        methods: {
            init_api: function() {
                api_data_for_scheduler_tasks().then((api_result) => {
                    success_prompt('update task successful~', 500);
                    this.scheduler_tasks = api_result.data;
                })
            },
            add_task: function() {
                scheduler_task_template.model = 'add';
                scheduler_task_template.task_info = {trigger: 'cron'};
            },
            open_task: function(taskID) {
                axios.post(`/scheduler/jobs/${taskID}/resume`).then(() => {
                    this.init_api();
                })
            },
            close_task: function(taskID) {
                axios.post(`/scheduler/jobs/${taskID}/pause`).then(() => {
                    this.init_api();
                })
            },
            edit_task: function(task_info) {
                scheduler_task_template.model = 'edit';
                scheduler_task_template.task_info = task_info;
            },
            delete_task: function(task) {
                if (confirm('still delete this task?')) {
                    api_data_for_deleting_task(task.id).then(() => this.init_api());
                }
            }
        },
    });
    var scheduler_task_template = new Vue({
        el: '#scheduler_task_template',
        delimiters: ['[[', ']]'],
        data: {
            task_info: '',
            model: '',
        },
        methods: {
            click_button: function() {
                if (this.model === 'edit') {
                    this.edit_task();
                } else if (this.model === 'add') {
                    this.add_task();
                } else {
                    danger_prompt('there is some error! please contact for manager', 1000);
                }
            },
            edit_task: function() {
                data = {"trigger": "cron"};
                if (this.task_info.hour) { data['hour'] = this.task_info.hour };
                if (this.task_info.minute) { data['minute'] = this.task_info.minute };
                if (this.task_info.second) { data['second'] = this.task_info.second };
                if (data) {
                    api_data_for_patch_task(this.task_info.id, data).then(() => {
                        this.clear_task();
                        page_4.init_api();
                    })
                }
            },
            add_task: function() {
                data = {
                    id: this,
                    name: this,
                    func: this,
                    kwargs: {task_name: this},
                    trigger: 'cron',
                    hour: this.null,
                    minute: null,
                    second: null,
                }
                if (!(this.task_info.id || this.task_info.name || this.task_info.func || this.task_info.task_name)) {
                    danger_prompt('input error!', 1000);
                    return
                }
                this.task_info.kwargs = {
                    task_name: this.task_info.task_name
                };
                delete this.task_info.task_name;
                console.log(this.task_info)
                return
                api_data_for_add_task(data).then(() => this.init_api())
            },
            clear_task: function() {
                this.model = '';
                this.task_info = '';
            },
        },
    });
    // fifth tab panel
    new Vue({
        el: '#page-5',
        delimiters: ['[[', ']]'],
        data(){
            return {
                logs: []
            }
        },
        mounted(){
            this.init_api();
        },
        methods: {
            init_api: function() {
                api_data_for_logs().then((api_result) => {
                    success_prompt('update logs successful~', 500);
                    this.logs = api_result.data;
                })
            },
        },
    });
})
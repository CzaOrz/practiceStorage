$(function(){
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
    var
        api_data_get_lottery_count = () => axios.get('http://127.0.0.1:5000/api/get/lottery/count'),
        api_data_add_lottery_price = (data) => axios.post('http://127.0.0.1:5000/api/add/lottery', data);
    new Vue({
        el: "#show-lottery",
        delimiters: ['[[', ']]'],
        data(){
            return {
                lottery_username: null,
                lottery_num: null,
                tema_num: null,
                lottery_price: null,
                lottery_count: [],
                lottery_sort: [],
                history_data: [],
                fix_data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            }
        },
        mounted(){
            api_data_get_lottery_count().then((api_result) => {
                this.init_data(api_result.data);
//                this.lottery_count = api_result.data.lottery_count;
            })
        },
        methods: {
            init_data: function(api_result){
                history_store = [];
                for (key in api_result){
                    if (key === 'history_data'){
                        for (data in api_result[key]){
                            for (username in api_result[key][data]){
                                value = api_result[key][data][username];
                                for (lot in value) {
                                    log_info = `特码-${lot}: ${value[lot]}  -- ${username}`;
                                    history_store.push(log_info);
                                }
                            }
                        }
                    }
                }
                this.history_data = history_store;
            },
            add_data: function(){
                lottery_num = this.lottery_num;
                lottery_price = this.lottery_price;
                if (lottery_num && lottery_price) {
                    api_data_add_lottery_price({
                        username: this.lottery_username,
                        lottery_num: this.lottery_num,
                        lottery_price: this.lottery_price
                    }).then((api_result) => {
                        this.lottery_count = api_result.data.lottery_count;
                        success_prompt("add successful");
                    })
                }
            },
        },
    })
})

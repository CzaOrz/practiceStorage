$(window).scroll(function(){
　　var scrollTop = $(this).scrollTop();
　　var scrollHeight = $(document).height();
　　var windowHeight = $(this).height();
　　if(scrollTop + windowHeight + 1 > scrollHeight){
　　　　app.loading_blog();
　　}
});

var app = new Vue({
    el: '#app',
    created(){
        this.loading_settings()
    },
    mounted(){
        this.$refs.search_box.onfocus = () => { this.search_flag = true; }
        this.$refs.search_box.onblur = () => {
            if (!this.search_content){
                this.search_flag = false;
            }
        }
    },
    data:{
        settings: {},
        search_flag: false,
        search_content: '',
        all_blogs: []
    },
    methods: {
        async loading_settings(){
            let json_data = await axios.get('./settings.json')
            this.settings = json_data.data
        },
        async loading_blog(){
            let json_data = await axios.get(this.settings.blog_url)
            this.all_blogs = json_data.data
        },
    },
})
<template>
    <div class="wrap-article">
        <ul id="content">
            <li class="article" v-for="item in article_list">
                <div class="article-wrap">
                    <div class="article-img">
                        <a href="javascript:;"><img v-bind:src="item.imgs"></a>
                    </div>
                    <div class="article-content clearfix">
                        <h1><a href="javascript:;">{{ item.title }}</a></h1>
                        <p class="time">{{ item.created | datetime }}</p>
                        <p class="author">{{ item.author }}</p>                         
                    </div>                   
                </div>
            </li>
        </ul>
    </div>
</template>
<script>
    export default {
        data: function(){
            return {
                apiUrl: "http://127.0.0.1:9000/api/article_list",
                article_list: null,
            }
        },
        mounted: function(){
            this.getData()
        },
        methods: {
            getData: function(){
                this.$http.get(this.apiUrl).then(function(response){
                    const data = response.body;
                    this.article_list = data;
                },function(response){
                    console.log('error')
                });             
            }
        },
        computed: {

        }
    }
</script>

<style scoped>
    .wrap-article {
        max-width: 1000px;
        margin: 20px auto 0 auto;
    }

    #content {
        width: 680px;
        padding-right: 30px;
    }

    .article {
        width: 680px;
        height: 180px;
        padding: 30px 0 30px 0;
        border-bottom: 1px solid #e8e4e4;
        font-family: Source Sans Pro,Helvetica Neue,Arial,sans-serif;
    }

    .article:hover ,.article:visited {
        background-color: #F5F4F4;
    }

    .article-wrap {
        position: relative;
        width: 100%;
        height: 180px;
    }

    .article-wrap .article-img {
        display: inline-block;
        height: 100%;
    }

    .article-img img {
        width: 200px;
        height: 100%;
    }

    .article-content {
        position: absolute;
        top: 0px;
        height: 100%;
        margin-left: 220px;
    }

    .article-content > h1 {
        font-size: 1.6em;
        color: #555555;
    }

    .article-content > h1 a:hover {
        color: #f84d4d;
    }

    .time {
        margin-top: 15px;
        font-size: 14px;
        color: #888;
    }

    .author {
        font-size: 14px;
        position: absolute;
        bottom: 10px;
        border: 1px solid #bfbfbf;
        border-radius: 10px;
        display: inline-block;
        padding: 5px 10px;
        color: #A9A9A9;
    }

</style>
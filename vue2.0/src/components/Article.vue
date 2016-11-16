<template>
    <div class="article">
        <div class="header">
            <h1>{{ news.title }}</h1>
            <p>
                <span>{{ news.created | datetime }} </span>
                <span>{{ news.newsItem }}</span>
            </p>
        </div>
    	<div class="content">
            <div v-html="news.article"></div>
        </div>
        <Loading v-show="load"></Load>   
    </div>
</template>
<script>
    import Loading from './Loading.vue'
    import { mapGetters, mapActions } from 'vuex'

    export default {
        components: {
            Loading
        },
        created: function(){
            this.getArticle(this);
        },
        computed: {
          ...mapGetters([
                'news',
                'load',
            ]),
        },

        methods: {
          ...mapActions([
                'getArticle',
            ]),     
        },
    }
</script>
<style scoped>
    .article {
        margin-top: 40px;
        font-family: "Microsoft YaHei";
    }
    
    .header {
        padding-bottom: 15px;
        border-bottom: 1px solid #e2e2e2;
    }

    .header > h1 {
        font-size: 30px;
        font-weight: normal;
        color: #222;
    }

    .header > p {
        margin: 30px 0 0 0;
        color: #999;
        text-indent: 0.2em !important;
    }

    .header > p > span {
        margin-right: 10px;
    }

    .content {
        margin-top: 30px;
        word-spacing: 0.05em;
        font-size: 1.1em;
        line-height: 1.8;
        color: #686868;
    }

    @media screen and (max-width: 855px){
        .article {
            box-sizing:border-box;
            -webkit-box-sizing:border-box;
            padding: 20px;
        } 

        .header > h1 {
            font-size: 20px;
        }

        .header > p {
            margin: 10px 0 0 0;
            font-size: 12px;
        }

    }

    @media screen and (max-width: 500px){
        .article {
            padding: 10px;
        }
    }

</style>
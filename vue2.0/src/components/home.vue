<template>
    <div class="section">
        <ul id="content">
            <li class="article" v-for="item in NewsList">
                <div class="article-wrap">
                    <div class="article-img">
                        <router-link :to="{ name: 'id', params: { id: item.id } }"
                            <img v-bind:src="item.imgs" />
                        </router-link>
                    </div>
                    <div class="article-content clearfix">
                        <h1><router-link :to="{ name: 'id', params: { id: item.id } }">{{ item.title }}</router-link></h1>
                        <p class="time">{{ item.created | datetime }}</p>
                        <p class="author">{{ item.author }}</p>                         
                    </div>                   
                </div>
            </li>
        </ul>
        <Loading v-show="Loading"></Loading>
        <div v-on:click="upDataNewsList" class="more" v-show="More" v-text="MoreText"></div>
    </div>
</template>
<script>
    import Loading from './Loading.vue';
    import { mapGetters, mapActions } from 'vuex';

    export default {
        components: {
            Loading
        },
        created: function(){
            this.getNewsList(this);
        },

        computed: {
          ...mapGetters([
                'NewsList',
                'Loading',
                'More',
                'MoreText',
            ]),
        },

        methods: {
          ...mapActions([
                'getNewsList',
                'upDataNewsList'
            ]),            
        },

        watch: {
            '$route': function(){
                this.getNewsList(this);
            }
        }
    }
</script>

<style scoped>
    #content {
        width: 100%;
        padding-right: 30px;
    }

    .article {
        width: 100%;
        height: 180px;
        padding: 30px 0 30px 0;
        border-bottom: 1px solid #e8e4e4;
        font-family: Source Sans Pro,Helvetica Neue,Arial,sans-serif;
    }

    .article:hover ,.article:active {
        background-color: #F5F4F4;
    }

    .article-wrap {
        position: relative;
        width: 100%;
        height: 180px;
    }

    .article-wrap .article-img {
        float: left;
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
    }

    .article-content p {
        text-indent: 0 !important;
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
        margin: 0 !important;
    }

    .more {
        margin-top: 15px;
        padding: 15px 0;
        font-size: 1.2em;
        text-align: center;
        background-color: #F0EFEF;
        cursor: pointer;
    }

    .more:hover {
        background-color: #DFDFDF;
        color: #f84d4d;
    }

    @media screen and (max-width: 855px){
        #content {
            box-sizing:border-box;
            -webkit-box-sizing:border-box;
            padding: 20px 25px !important;
        }

        .article-content > h1 {
            font-size: 1.3em !important;
        }

        .article-content > h1 a {
            color: #525252;
        }
        
        .more {
            margin: 0 10px !important;
            font-size: 1.1em;
        }

        .more:active {
            background-color: #F7F7F7;
        }       
    }

    @media screen and (max-width: 500px){

        #content {
            box-sizing:border-box;
            -webkit-box-sizing:border-box;
            padding: 10px 10px !important;
        }

        .article {
            width: 100% !important;
            height: 140px !important; 
            padding: 20px 0 !important;
        }        

        .article-wrap {
            height: 140px !important;
        }

        .article-img img {
            width: 140px !important;
        }

        .article-content {
            margin: 0px !important;
            left: 150px !important;
            min-width: calc(100% - 150px);
        }

        .article-content > h1 {
            font-size: 1.1em !important;
        }

        .article-content > h1 a:hover {
            color: #525252;
        }

        
        .time {
            font-size: 12px !important;
        }

        .author {
            font-size: 12px !important;
            border-radius: 5px;
            padding: 3px 8px;
        }

        .more {
            margin: 0 10px !important;
            font-size: 1em;
            background-color: white;
        }

        .more:active {
            background-color: #F7F7F7;
            color: #525252;
        }
    }

    @media screen and (max-width: 320px){
        .article-img img {
            width: 120px !important;
        } 

        .article-content {
            margin: 0px !important;
            left: 130px !important;
        }  
    }
</style>
<template>
    <div class="wrap">
        <Headers class="header" v-bind:eventData="eventData"></Headers>
        <div class="main" v-bind:class="[ eventData.scrollTop >= eventData.logoHeight ? 'main-scroll' : '']">
            <transition :name="transitionName">
                <router-view class="body view"></router-view>
            </transition>
        </div>
        <Backtop v-show="scrollShow" v-tap="{ methods: backtop }"></Backtop>
    </div>
</template>

<script type="text/babel">
    import './assets/font-awesome-4.6.3/css/font-awesome.min.css';
    import Headers from 'components/Headers.vue';
    import Backtop from 'components/Backtop.vue';
    import { mapGetters, mapActions } from 'vuex';

    export default {
        components: {
            Headers,
            Backtop
        },

        data: function(){
            return {
                scrollShow: false,
                timer: null,
                flag: true,
                transitionName: 'slide-left',
                pathList: [],
                eventData: {
                    scrollTop: "",
                    logoHeight: 0,
                    width: document.body.clientWidth
                },
            }
        },
        mounted: function(){
            const self  = this;
            let timer = null;

            this.eventData.moveX = false; 
            this.eventData.logoHeight = document.getElementsByClassName("logo")[0].clientHeight;
            this.getScrollTop();
            window.addEventListener('resize', function(){
                timer && clearTimeout(timer);
                timer = setTimeout(function(){
                    self.eventData.width = document.body.clientWidth;  
                    self.getMoveX(0)            
                },50)

                self.eventData.logoHeight = document.getElementsByClassName("logo")[0].clientHeight;
            });
        },

        watch: {
           '$route' (to, from) {
                this.$store.commit('REST_CACHE')
                const toDepth = to.path.split('/').length
                const fromDepth = from.path.split('/').length

                // 收集路由路径存入数组,并限制最大长度
                this.pathList.push(to.path)
                if (this.pathList.length >3){
                    this.pathList.shift()
                }

                // 根据路由来判断是否利用vuex 缓存
                if (this.pathList.length>1 && this.pathList.indexOf(to.path) === 0 && toDepth !== fromDepth){
                    this.$store.commit('CACHE')
                }
                this.transitionName = toDepth < fromDepth ? 'slide-right' : 'slide-left'
            }
        },

        methods: {
            ...mapActions([
                'getMoveX',
            ]),

            getScrollTop: function(){
                let self = this;
                document.addEventListener("scroll",function(){
                    self.eventData.scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
                    (self.eventData.scrollTop>800)?(self.scrollShow = true):(self.scrollShow = false);
                    if (!self.flag) {
                        clearInterval(self.timer);
                    }
                    self.flag = false

                })
            },
            backtop: function(){
                let scrollTop;
                let self = this;
                this.timer = setInterval(function(){
                    scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
                    let Speed=Math.floor(-scrollTop/6)
                    if (scrollTop <= 0) {
                        clearInterval(self.timer);
                        
                    } else {
                        self.flag = true;
                        document.documentElement.scrollTop=document.body.scrollTop=scrollTop+Speed;
                    } 
                },20);
                
            },
        }
    }
</script>

<style>
    body,ol,ul,li,h1,h2,h3,h4,h5,h6 {
        margin: 0;
        padding: 0;
    }
    
    h1,h2,h3,h4,h5,h6 {
        font-size: 0.16rem;
    }

    p {
        text-indent: 2em;

    }

    img {
        width: 100%;
    }

    .clearfix:after {
        content: "."; 
        display: block; 
        height: 0; 
        clear: both; 
        visibility: hidden;  
    }

    .clearfix {
        zoom: 1; 
    }

    body {
        color: #555;
        font-size: 14px;
        font-family: "Microsoft Yahei";
        word-spacing: 0.05em;
        -webkit-tap-highlight-color:transparent;
        overflow-x: hidden;
    }

    a {
        text-decoration: none;
        color: #1B1B1B;
        -webkit-tap-highlight-color:transparent;
        cursor: pointer;
    }

    ul,ol {
        list-style: none;
    }

    .main {
        max-width: 1000px;
        margin: 0 auto;
    }

    .main-scroll {
        margin-top: 60px;
    }

    .body {
        width: 680px;
        position: relative;
        margin: 20px 0 400px 0;
    }

    .view {
        opacity: 1;
        position: absolute;
        transition: transform .4s cubic-bezier(.55,0,.1,1);
    }

    .slide-left-enter, .slide-right-leave-active {
        opacity: 0;
        -webkit-transform: translate(50px, 0);
        transform: translate(50px, 0);
    }

    .slide-left-leave-active, .slide-right-enter {
        opacity: 0;
        -webkit-transform: translate(-50px, 0);
        transform: translate(-50px, 0);
    }

    @media screen and (max-width: 840px) {
        .body {
            width: 100% !important;
            margin: 0 !important;
        }

        .slide-left-enter, .slide-right-leave-active {
            opacity: 0;
            -webkit-transform: translate(100%, 0);
            transform: translate(100%, 0);
        }

        .slide-left-leave-active, .slide-right-enter {
            opacity: 0;
            -webkit-transform: translate(-100%, 0);
            transform: translate(-100%, 0);
        }

        .main-scroll {
            margin-top: 50px !important;
        }
    }
</style>
<template>
    <div class="header">
        <div class="logo">
            <router-link to="/">
                <img src="../assets/img/logo.png">
            </router-link>
            <div class="login">
                <span> <i class="fa fa-user fa-2x"></i>登录</span>
            </div>
        </div>
        <nav class="nav" v-bind:class="[ eventData.scrollTop >= eventData.logoHeight ? 'active' : ''] ">
            <div class="nav-wrap">
                <ul class="list" @touchstart="touchStart" @touchmove="touchMove" @touchend="touchEnd"
                                v-bind:style="{ transform: 'translate3d('+ moveX + 'px,0,0)'}">
                    <li v-for="(value, key) in navList">
                        <router-link :to="{ name:'item' , params: { item: key } }">{{ value }}</router-link>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
    import { mapGetters, mapActions } from 'vuex';

    export default {
        props: ['eventData'],

        data: function(){
            return {
                navList: {
                    "redian": "热点",
                    "yule": "娱乐",
                    "tiyu": "体育",
                    "keji": "科技",
                    "hulianwang": "互联网",
                    "kexue": "科学",
                    "meishi": "美食",
                    "dianying": "电影",
                    "shehui": "社会",
                    "xingzuo": "星座"
                },
                slide: {
                    width: this.eventData.width,
                    startX: 0,
                    endX: 0, 
                    // moveX: this.moveX,
                },
            }
        },

        computed: {
          ...mapGetters([
                'moveX',
            ]),
        },

        methods: {
            ...mapActions([
                'getMoveX',
            ]),     

            touchStart: function(event){
                this.startX = event.touches[0].clientX - this.moveX;
            },

            touchMove: function(event){
                event.preventDefault();
                this.getMoveX(event.touches[0].clientX - this.startX);
            },

            touchEnd: function(event){
            	let minWidth = -this.eventData.width;
            	let maxWidth = 0;

            	if (this.moveX < minWidth){
            		this.getMoveX(- this.eventData.width);
            	}else if (this.moveX > 0){
            		this.getMoveX(0);
            	}
            },

        },
    }
</script>

<style scoped>
    .logo {
        margin: 0 auto;
        max-width: 1000px;
        height: 100px;
        position: relative;
    }
    
    .logo  img {
        vertical-align: middle;
        width: 146px;
        height: 66px;
    }

    .logo .login {
        position: absolute;
        top: 0;
        right: 0;
        line-height: 100px;
        cursor: pointer;
    }

    .login > span {
        display: inline-block;
        margin-right: 15px;
    }

    .login i {
        margin-right: 10px;
    }

    .nav-wrap {
        max-width: 1000px;
        margin: 0 auto;
    }

    .nav {
        position: relative;
        overflow: hidden;
        width: 100%;
        height: 60px;
        background-color: #F5F5F5;
        font-size: 16px;
    }

    .active {
        position: fixed;
        top: 0;
        z-index: 100;
    }

    .list {   
        position: absolute;

    }

    .phone-nav {
        display: none;
    }

    .list li {
        font-family: "Microsoft Yahei";
        float: left;
        line-height: 60px;
        display: inline-block;
    }

    .list li a {
        display: inline-block;
        padding: 0 25px;
    }

    .list li a:hover {
        color: #FB4747;
    }

    .router-link-active {
        color: #FB4747 !important;
    }

    @media screen and (max-width: 855px){
        .login {
            display: none;
        }

        .logo {
            height: 40px;
            background-color: #f84d4d;
        }

        .logo img {
            height: 40px !important;
        }

        .list {
            height: 100%;
        }

        .nav {
            width: 100%;
            height: 50px;
        }

        .list {
            width: 100%;
        } 

        .list li a {
            padding: 0!important;
        }

        .list li {
            width: 10%;
            text-align: center;
            line-height: 50px;
        }

        .router-link-active {
            border-bottom: 2px solid #FB4747;
        }
    }

    @media screen and (max-width: 500px){
        .nav {
            width: 100%;
            font-size: 15px;
        }
        .list {
            width: 200%;
            height: 40px!important;
        }

        .list li {
            width: 10%;
            line-height: 40px!important;
            text-align: center;
        }
    }
</style>
import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import App from './App.vue'
import store from './vuex/index'
import VueTap from 'v-tap'

Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(VueTap)

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/', 
            name: 'home',
            component: resolve => require(['./components/Home.vue'], resolve)
        },
        {
            path: '/:item',
            name: 'item',
            component: resolve => require(['./components/Home.vue'], resolve)
        },
        {
            path: '/article/:id',
            name: 'id',
            component: resolve => require(['./components/Article.vue'], resolve)
        },
        // { 
        //     path: '/',
        //     redirect: 'home'
        // },
    ],
    scrollBehavior (to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        } else {
            return { x: 0, y: 0 }
        }
    }
}) 


Vue.filter('datetime',function(value) {
    const date = new Date(new Date(value).valueOf());
    let Seconds = date.getSeconds()<10 ? ("0" + date.getSeconds()) : date.getSeconds();
    let Minutes = date.getMinutes()<10 ? ("0" + date.getMinutes()) : date.getMinutes();
    let Hours = date.getHours()<10 ? ("0" + date.getHours()) : date.getHours();
    let Day = date.getDate()<10 ? ("0" + date.getDate()) : date.getDate();
    let Month = date.getMonth() + 1 <10 ? ("0" + date.getMonth() + 1) : date.getMonth() + 1;
    return date.getFullYear() + "年" + Month + "月" + Day + "日" + " " + Hours + ":" + Minutes + ":" + Seconds
});

const app = new Vue({
  router: router,
  store : store,
  render: h => h(App)
}).$mount("#app")

import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import VueResource from 'vue-resource'
import App from './App.vue'

Vue.use(VueRouter)
Vue.use(Vuex)
Vue.use(VueResource)

const store = new Vuex.Store({
    
})


const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/', 
            name: 'home',
            component: function(resolve) {
                require(['./components/Home.vue'], resolve)
            }
        },
        {
            path: '/:item',
            name: 'item',
            component: function(resolve) {
                require(['./components/Home.vue'], resolve)
            }
        },
        { 
            path: '*',
            redirect: '/home'
        },
    ]
}) 

// Vue.filter('imgUrl',function(value){
//     let str = value.toString(); 
//     let arr = str.split("/");
//     let str1 = arr.splice(3,1);
//     let result = arr.join("/");
//     return value
// });

Vue.filter('datetime',function(value) {
    const date = new Date(new Date(value).valueOf());
    let Seconds = date.getSeconds()<10 ? ("0" + date.getSeconds()) : date.getSeconds();
    return date.getFullYear() + "年" + (date.getMonth()+1) + "月" + date.getDate()+ "日" + " " + date.getHours() + ":" +date.getMinutes() + ":" + Seconds
});

const app = new Vue({
  router: router,
  store : store,
  render: h => h(App)
}).$mount("#app")
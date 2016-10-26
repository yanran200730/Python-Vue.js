import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import VueResource from 'vue-resource'
import App from './App.vue'

Vue.use(VueRouter)
Vue.use(Vuex)
Vue.use(VueResource)

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/home', 
            component: function(resolve) {
                require(['./components/Home.vue'], resolve)
            }
        },
        { path: '*', redirect: '/home'},
        // {
        //     path: '/bar', 
        //     component: function(resolve) {
        //         require(['./components/bar.vue'], resolve)
        //     }
        // }
    ]
}) 

Vue.filter('imgUrl',function(value){
    let str = value.toString(); 
    let arr = str.split("/");
    let str1 = arr.splice(3,1);
    let result = arr.join("/");
    return value
});

const app = new Vue({
  router: router,
  render: h => h(App)
}).$mount("#app")
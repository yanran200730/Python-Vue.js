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
                require(['./components/home.vue'], resolve)
            }
        },
        // {
        //     path: '/bar', 
        //     component: function(resolve) {
        //         require(['./components/bar.vue'], resolve)
        //     }
        // }
    ]
}) 

const app = new Vue({
  router: router,
  render: h => h(App)
}).$mount("#app")

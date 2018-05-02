/*
* @Author: wangfpp
* @Date:   2018-04-25 16:11:10
* @Last Modified by:   wangjb
* @Last Modified time: 2018-05-02 16:11:42
*/
import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: resolve => require(['@/router/login'],resolve)
    },
    {
      path: '/home',
      name: 'home',
      component: resolve => require(['@/router/home/home.vue'], resolve)
    },
    {
      path: '/detail',
      name: 'detail',
      component: resolve => require(['@/router/detail/newsDetail.vue'],resolve)
    },
    {
      path: '/register',
      name: 'register',
      component: resolve => require(['@/router/register.vue'],resolve)
    }
  ]
})
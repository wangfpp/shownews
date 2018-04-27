/*
* @Author: wangfpp
* @Date:   2018-04-25 16:11:10
* @Last Modified by:   wangfpp
* @Last Modified time: 2018-04-27 15:52:43
*/
import Vue from 'vue'
import Router from 'vue-router'
import register from '@/router/register.vue'
import login from '@/router/login'
import home from '@/router/home.vue'
import detail from '@/router/newsDetail.vue'


Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/detail',
      name: 'detail',
      component: detail
    },
    {
      path: '/register',
      name: 'register',
      component: register
    }
  ]
})
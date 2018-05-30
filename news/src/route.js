/*
* @Author: wangfpp
* @Date:   2018-04-25 16:11:10
* @Last Modified by:   wangfpp
* @Last Modified time: 2018-05-30 20:43:20
*/
import Vue from 'vue'
import Vuex from 'vuex'
import Router from 'vue-router'
import news from '@/router/news/news.vue'
import user from '@/router/user/user.vue'
import chart from '@/router/chart/chart.vue'
Vue.use(Router)
Vue.use(Vuex)
export default new Router({
  routes: [
     {
      path: '/',
      name: 'login',
      component: resolve => require(['@/router/login'],resolve),
      site : true
    },
    {
      path: `/home`,
      name: 'home',
      component: resolve => require(['@/router/home/home.vue'], resolve),
      redirect:`/home/news`,
      site : true,
      children : [
        {
          path : `/home/news`,
          name : 'news',
          component : news,
          site : true
        },
        {
          path : '/home/user',
          name : 'user',
          component : user
        },
        {
          path : '/home/chart',
          name : 'chart',
          component : chart
        },
        {
          path: '/home/detail',
          name: 'detail',
          component: resolve => require(['@/router/detail/newsDetail.vue'],resolve)
        },
      ]
    },
    
    {
      path: '/register',
      name: 'register',
      component: resolve => require(['@/router/register.vue'],resolve)
    }
  ]
})
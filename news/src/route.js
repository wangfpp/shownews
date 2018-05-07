/*
* @Author: wangfpp
* @Date:   2018-04-25 16:11:10
* @Last Modified by:   wangjb
* @Last Modified time: 2018-05-04 12:23:41
*/
import Vue from 'vue'
import Vuex from 'vuex'
import Router from 'vue-router'
import news from '@/router/news/news.vue'
import user from '@/router/user/user.vue'
Vue.use(Router)
Vue.use(Vuex)
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
      component: resolve => require(['@/router/home/home.vue'], resolve),
      redirect:'/home/news',
      children : [
        {
          path : '/home/news',
          name : 'news',
          component : news
        },
        {
          path : '/home/user',
          name : 'user',
          component : user
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
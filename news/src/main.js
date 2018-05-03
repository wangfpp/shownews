// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import vuex from 'vuex'
import store from '@/config/store.js' 
import router from './route.js'
import iView from 'iview' 
import 'iview/dist/styles/fonts/ionicons.eot'
import 'iview/dist/styles/fonts/ionicons.svg'
import 'iview/dist/styles/fonts/ionicons.ttf'
import 'iview/dist/styles/fonts/ionicons.woff'
import 'iview/dist/styles/iview.css'
Vue.config.productionTip = false
import {Message} from 'iview'
Vue.prototype.$Message = Message
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})


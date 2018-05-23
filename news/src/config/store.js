/*
* @Author: wangjb
* @Date:   2018-05-02 17:15:49
* @Last Modified by:   wangfpp
* @Last Modified time: 2018-05-23 15:25:41
*/
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
export default new Vuex.Store({
	state : {
		user : {
			userName : '',
			phonenum : ''
		},
		theme : 'dark',
		count : 0,
		city : '青岛'
	}
})

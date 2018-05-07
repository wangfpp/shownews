/*
* @Author: wangjb
* @Date:   2018-05-02 17:15:49
* @Last Modified by:   wangjb
* @Last Modified time: 2018-05-05 22:52:03
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
		count : 0
	}
})

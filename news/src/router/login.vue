<template>
	<div id = "login">
		<input type="text" v-model="phonenum" placeholder="手机号"> 
		<input type="password" v-model = "password" placeholder="密码">
		<button v-on:click = "login"> 登录</button>
		<br/>
		<button v-on:click = "jump()">注册</button>
	</div>
</template>

<script type="text/javascript">
import { mainServer } from 'server/mainserver.js'
	export default {
		name : 'login',
		data () {
			return {
				phonenum : '',
				password : ''
			}
		},
		components : {

		},
		methods : {
			login (){
				let _this = this;
				mainServer.login({phonenum : _this.phonenum, password : _this.password}).then( res => {
					console.log(res);
					_this.$router.push({
						name : 'home'
					})
				}, err => {
					console.log(err)
				})
			},
			jump (){
				this.$router.push({
					name : 'register'
				})
			}
		},
		mounted () {
			let _this = this;
			mainServer.prelogin().then( res => {
				this.$router.push({
					name : 'home'
				})
			}, err => {
				console.log(err)
			})
		}
	}
</script>

<style  scoped>

</style>
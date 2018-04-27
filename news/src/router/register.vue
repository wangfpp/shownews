<template>
	<div id = "register">
		<label for="phonenum">
			手机号:<input type="text" v-model = "phonenum" placeholder="手机号">
		</label>
		<br/>
		<label for="username">
			用户名:<input type="text" v-model = "username" placeholder="用户名">
		</label>
		<br/>
		<label for="password">
			 密 码 :<input type="password" v-model = "password" placeholder="密码">
		</label>
		<br/>
		<button v-on:click = "register()">注册</button>
	</div>
</template>

<script type="text/javascript">
import { mainServer } from 'server/mainserver.js'
	export default {
		name : 'register',
		data () {
			return {
				phonenum : '',
				username : '',
				password : ''
			}
		},
		components : {

		},
		methods : {
			register (){
				let _this = this;
				mainServer.register({phonenum: _this.phonenum, username : _this.username,password : _this.password}).then( res =>{
					_this.$router.push({
						name : 'login'
					})
				}, err => {
					console.log(err)
				})
			}
		},
		beforeCreate () {

		}
	}
</script>

<style scoped>

</style>
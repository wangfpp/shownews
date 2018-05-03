<template>
	<div id = "login">
		<Form ref="formInline" :model="formInline" :rules="ruleInline" :label-width="80">
        <FormItem prop="phonenum">
            <Input type="text" v-model="formInline.phonenum" placeholder="用户名">
                <Icon type="ios-person-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        
        <FormItem prop="password">
            <Input type="password" v-model="formInline.password" placeholder="密码">
                <Icon type="ios-locked-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        
        <FormItem>
            <Button type="primary" @click="handleSubmit('formInline')">登录</Button>
        </FormItem>
     	<span>无账号去<a v-on:click="jump">注册</a> </span>
     	<span>{{count}}</span>
    </Form>
	</div>
</template>

<script type="text/javascript">

import { mainServer } from 'server/mainserver.js'
import { Form, FormItem, Input, Icon, Button } from 'iview'
import { mapState } from 'vuex'
	export default {
		name : 'login',
		 data () {
	        return {
	            formInline: {
	                phonenum: '',
	                password: ''
	            },
	            ruleInline: {
	                user: [
	                    { required: true, message: '请输入用户名', trigger: 'blur' }
	                ],
	                password: [
	                    { required: true, message: '请输入密码', trigger: 'blur' },
	                    { type: 'string', min: 6, message: '至少6个字符', trigger: 'blur' }
	                ]
	            }
	       }
	    },
	    computed : {
	    	count () {
	    		return this.$store.state.count;
	    	}
	    },
		components : {
			FormItem,
			Form,
			Input,
			Icon,
			Button
		},
		methods : {
			login (){
				let _this = this;
				mainServer.login({phonenum : _this.formInline.phonenum, password : _this.formInline.password}).then( res => {
					_this.$store.state.user.userName = res.data.username
					_this.$router.push({
						name : 'home'
					})
				}, error => {
					//if(error.response.status == 403){
						_this.$Message.error('登录失败');
					//}
					
				})
			},
			jump (){
				this.$router.push({
					name : 'register'
				})
			},
			handleSubmit(name) {
				let _this = this;
                this.$refs[name].validate((valid) => {
                    if (valid) {
                    	this.login()
                        //_this.$Message.success('Success!');
                    } else {
                        _this.$Message.error('Fail!');
                    }
                })
            }
		},
		mounted () {
			let _this = this;
			console.log(this.$store.state.user.userName)
			// mainServer.prelogin().then( res => {
			// 	this.$router.push({
			// 		name : 'home'
			// 	})
			// }, err => {
			// 	console.log(err)
			// })
		}
	}
</script>

<style  scoped>
	@import '../static/css/login.scss';
</style>
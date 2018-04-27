<template>
	<div id = "detail">
		详情页
		<div v-for=" item in newsDetail">
			<p v-for="(value,key) in item">
				<template v-if ="key == 'name'">
					<h2>{{value}}</h2>
				</template>
				<textarea id="textdetail" name="content" cols="80" rows="10" v-if = "key == 'text'" :value = "value"></textarea>
			</p>
		</div>
		<br/>
		<button v-on:click = "updateText()">更新</button>
	</div>
</template>

<script type="text/javascript">
import { mainServer } from 'server/mainserver.js'
	export default {
		name : 'detail',
		data () {
			return {
				id : '',//路由传参的id
				newsDetail : '',
			}
		},
		components : {

		},
		methods : {
			updateText (){
				let _this = this;
				let text = document.getElementById('textdetail').value;
				mainServer.updateNews({id:_this.id,text:text}).then( req => {
					console.log(req)
				}, err => {
					console.log(err)
				})
			}
		},
		mounted () {
			let _this = this
			this.id = this.$route.query.id
			mainServer.controlNews({params:{id : _this.id}}).then( req =>{
				_this.newsDetail = req
			},err => {
				console.log(err)
			})

		}
	}
</script>

<style scoped>

</style>
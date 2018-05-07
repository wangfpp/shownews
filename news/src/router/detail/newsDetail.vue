<template>
	<div id = "detail">
		<!-- 详情页
		<div v-for=" item in newsDetail">
			<p v-for="(value,key) in item">
				<template v-if ="key == 'name'">
					<h2>{{value}}</h2>
				</template>
				<textarea id="textdetail" name="content" cols="80" rows="10" v-if = "key == 'text'" :value = "value"></textarea>
			</p>
		</div>
		<br/> -->
		<h3>详情页</h3>
		<div class="content">
			<Card :bordered ="true">
				<textarea id="textdetail" name="content" cols="80" rows="10" :value = "newsDetail['text']"></textarea>
			</Card>
		</div>
		
		<Button type="primary" shape="circle" v-on:click = "updateText()">更新</Button type="primary" shape="circle">
		<Spin fix v-if = "loading">加载中...</Spin>
	</div>
</template>

<script type="text/javascript">
import { mainServer } from 'server/mainserver.js'
import { Card ,Button, Spin, Col} from 'iview'
import html2canvas from 'html2canvas'
import axios from 'axios'
	export default {
		name : 'detail',
		data () {
			return {
				id : '',//路由传参的id
				newsDetail : '',
				loading : true,
				html : '',
			}
		},
		components : {
			Card,
			Button,
			Spin,
			Col
		},
		watch :{
			
		},
		methods : {
			updateText (){
				let _this = this;
				let text = document.getElementById('textdetail').value;
				mainServer.updateNews({id:_this.id,text:text}).then( req => {
					_this.getText({params:{id : _this.id}})
				}, err => {
					console.log(err)
				})
			},
			getText(params){
				let _this = this;
				mainServer.controlNews(params).then( req =>{
				_this.newsDetail = req[0];
				_this.loading = false;
			},err => {
				console.log(err)
			})
			}
		},
		mounted () {
			let _this = this
			this.id = this.$route.query.id
			_this.getText({params:{id : _this.id}})
			this.$nextTick(function(){
				mainServer.getOriginalNews('http://www.chinanews.com/gn/2018/05-04/8506380.shtml').then(res => {
					_this.html = res;
					console.log('aaa',_this.html)
				})
			})
				
	        //let node = document.createElement('html');
	        //node.innerHTML = _this.html;
	        //console.log(_this.html)
		}
	}
</script>

<style scoped>
	@import './detail.scss';
</style>
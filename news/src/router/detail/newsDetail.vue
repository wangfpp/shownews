<template>
	<div id = "detail">
		<h3>详情页</h3>
		<div class="content">
			<Card :bordered ="true">
				<textarea id="textdetail" name="content" cols="80" rows="10" :value = "newsDetail['text']"></textarea>
			</Card>
		</div>
		
		<Button type="primary" shape="circle" v-on:click = "updateText()">更新</Button type="primary" shape="circle">
		<Button type="primary" shape="circle" v-on:click = "origin_url()">跳转原网页</Button type="primary" shape="circle">
		<Spin fix v-if = "loading">加载中...</Spin>
		<img :src="img" alt="">
	</div>
</template>

<script type="text/javascript">
import { mainServer } from 'server/mainserver.js'
import { Card ,Button, Spin, Col} from 'iview'
import html2canvas from 'html2canvas'
import './detail.scss'
import axios from 'axios'
	export default {
		name : 'detail',
		data () {
			return {
				id : '',//路由传参的id
				newsDetail : '',
				loading : true,
				html : '',
				name : '',
				img : ''
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
			updateText (){//更新新闻/纠正新闻
				let _this = this;
				let text = document.getElementById('textdetail').value;
				mainServer.updateNews({id:_this.id,text:text}).then( req => {
					_this.getText({params:{id : _this.id}})
				}, err => {
					console.log(err)
				})
			},
			getText(params){//获取新闻信息
				let _this = this;
				mainServer.controlNews(params).then( req =>{
					console.log(req)
					_this.newsDetail = req[0];
					_this.loading = false;
				},err => {
					console.log(err)
				})
			},
			origin_url(){//跳转原新闻网页
				let originName = this.name.split('.')[0].replace(/\_/g,'/');
				let url = `http://www.chinanews.com/${originName}.shtml`
				window.open(url)
			}
		},
		mounted () {
			let _this = this
			this.id = this.$route.query.id
			this.name = this.$route.query.name
			_this.getText({params:{id : _this.id}})
			this.$nextTick(function(){
				mainServer.getOriginalNews('http://www.chinanews.com/gn/2018/05-04/8506380.shtml').then(res => {
				})
			})
			axios.get('api/img/').then(res => {
				_this.img = res.data
			})
				
		}
	}
</script>

<style scoped>
</style>














<template>
	<div id = "home">
		<table border="1">
			<tr>
				<th>名称</th>
				<th>类型</th>
				<th>大小</th>
				<th>内容</th>
				<th>日期</th>
			</tr>
			<tr v-for = "item in news">
				<td v-on:click = "jumpDetail(item.id)">{{item.name}}</td>
				<td>{{item.type}}</td>
				<td>{{item.size}}</td>
				<td>{{item.text}}</td>
				<td>{{item.time}}</td>
			</tr>
		</table>
	</div>
</template>

<script type="text/javascript">
import { mainServer } from 'server/mainserver.js'
import {Table,Page} from 'iview'
	export default {
		name : 'home',
		data () {
			return {
				news : '',
				current : 1,
				total : 0,

			}
		},
		components : {
			Table,
			Page
		},
		methods : {
			jumpDetail(id){
				this.$router.push({
					name : 'detail',
					query : {id : id}
				})
			}
		},
		mounted () {
			let _this = this;
			mainServer.getNews({page:_this.current,size:10}).then( res => {
				_this.news = res.data;
				_this.total = res.total;
				console.log(_this.news)
			})
		}
	}
</script>

<style  scoped>

</style>
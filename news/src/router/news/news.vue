<template>
	<div id = "news">
		<Table :data="news" :columns="tableColumns1" highlight-row stripe type='selection' :loading = "loading" @on-current-change="jumpDetail"></Table>
	    <div style="margin: 10px;overflow: hidden">
	        <div style="float: right;">
	            <Page :total="total" :current="current"  show-total v-on:on-change="changePage"></Page>
	        </div>
	    </div>
	</div>
</template>

<script type="text/javascript">
import { mainServer } from 'server/mainserver.js'
import { newsType } from 'server/en2ch.js'
import {Table,Page,Affix,Menu,MenuItem,Icon,MenuGroup,TabPane,Button} from 'iview'
	export default {
		name : 'news',
		data () {
			return {
				news : [],
				current : 1,
				total : 0,
				loading : true,
				tableColumns1 :[
					{title : '名称', key : 'name'},
					{title : '类型', key : 'type'},
					{title : '内容', key : 'text',type : 'html'},
					{title : '大小', key : 'size'},
					{title : '时间', key : 'time'},

				],

			}
		},
		components : {
			Table,Page,Affix,Menu,MenuItem,Icon,MenuGroup,TabPane,Button
		},
		methods : {
			jumpDetail(currentRow){
				this.$router.push({
					name : 'detail',
					query : {id : currentRow['id']}
				})
			},
			changePage(index){
				let _this = this;
				this.current = index;
				console.log(_this.current)
				this.getNewsList({params :{page:_this.current,size:10}})
			},
			getNewsList(params){
				let _this = this;
				mainServer.getNews(params).then( res => {
				res.data.forEach(item => {
					item['type'] = newsType[item['type']]				
				})
				_this.news = res.data;
				_this.total = res.total;
				_this.loading = false;
			})
			}

		},
		mounted () {
			let _this = this;
			this.getNewsList({params :{page:_this.current,size:10}})
		}
	}
</script>

<style lang = "scss" >
	@import './news.scss';
</style>
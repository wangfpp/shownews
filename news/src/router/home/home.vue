<template>
	<div id = "home">
		<div class="top">
			<ul>
				<li v-for="item in menu" :key="item.path">
					<router-link :to="item.path">{{item.text}}</router-link>
				</li>
				<li class="user">当前用户:{{$store.state.user.userName}}</li>
			</ul>
		</div>
		<div class="content">
			<router-view/>
		</div>
	</div>
</template>

<script type="text/javascript">
import {Affix,Menu,MenuItem,Icon} from 'iview'
	export default {
		name : 'home',
		data () {
			return {
				name : '',
				menu : [
					{
						text : '新闻列表',
						path : '/home/news'
					},
					{
						text : '用户管理',
						path : '/home/user'
					},
					{
						text : '报表统计',
						path : '/home/chart'
					}
				]
			}
		},
		components : {
			Affix,Menu,MenuItem,Icon
		},
		methods : {

		},
		mounted () {
			let _this = this;
			this.name = this.$store.state.user.userName
		}
	}
</script>

<style lang = "scss" >
@import './home.scss';
</style>
























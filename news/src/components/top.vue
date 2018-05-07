<template>
	<div id = "top">
		
	</div>
</template>

<script type="text/javascript">
import {Affix,Menu,MenuItem,Icon} from 'iview'
	export default {
		name : 'top',
		data () {
			return {
			}
		},
		components : {
			Affix,Menu,MenuItem,Icon
		},
		methods : {

		},
		mounted () {
			let _this = this;
		}
	}
</script>

<style lang = "scss" scoped>
$width : 100%;
#top{
	width:$width;
	height:60px;
	.top{
		height:100%;

	}
}
</style>
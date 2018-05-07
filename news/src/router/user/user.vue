<template>
	<div id = "user">
		当前用户:{{$store.state.user.userName + ',手机号' + $store.state.user.phonenum}}
	</div>
</template>

<script type="text/javascript">
	export default {
		name : 'user',
		data () {
			return {

			}
		},
		components : {

		},
		methods : {

		},
		beforeCreate () {

		}
	}
</script>

<style lang = "scss" scoped>

</style>
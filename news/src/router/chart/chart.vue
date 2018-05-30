<template>
	<div id = "chart">
		<div id="pie">
			
		</div>
	</div>
</template>

<script type="text/javascript">
import { mainServer } from 'server/mainserver.js'
import { newsType } from 'server/en2ch.js'
import echarts from 'echarts'
	export default {
		name : 'chart',
		data () {
			return {
				chart : '',
				results : [],//获取的数据[{type:''},{}]
			}
		},
		components : {

		},
		methods : {
			drawPie(id,data){
				let name = []
				data.forEach(item =>{
					name.push(item.name)
				})
				this.chart = echarts.init(document.getElementById(id));
				this.chart.setOption({
				    tooltip: {
				        trigger: 'item',
				        formatter: "{b}: {c} ({d}%)"
				    },
				    legend: {
				        orient: 'horizontal',
				        x: 'left',
				        y:'top',
				        data:name
				    },
				    series: [
				        {
				            type:'pie',
				            center : ['55%','55%'],
				            radius: ['40%', '70%'],
				            data:data
				        }
				    ]
				})
			}
		},
		mounted () {
			var _this = this;
			mainServer.getNews({params:{type:'chart'}}).then( res =>{
				let tmp = {}
				let current = ''
				res.data.forEach((item,i)=>{
					if(item.type == current){
						if(current in tmp){
							tmp[current] += 1;
						}else{
							tmp[current] = 1;
						}
					}else{
						current = item.type;
						if(current in tmp){
							tmp[current] += 1;
						}else{
							tmp[current] = 1;
						}
					}
				})
				for (var key in tmp){
					if(newsType[key]){
						_this.results.push({name : newsType[key], value : tmp[key]})	
					}else{
						_this.results.push({name : key, value : tmp[key]})
					}
					
				}
				console.log(_this.results)
				_this.drawPie('pie',_this.results)
			})
		}
	}
</script>

<style lang = "scss">
	@import './chart.scss'
</style>
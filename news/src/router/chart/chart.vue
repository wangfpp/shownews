<template>
	<div id = "chart">
		<div id="date">
			<DatePicker type="daterange" format="yyyy-MM-dd" conform="'true'" placeholder="Select date and time(Excluding seconds)" style="width: 300px" v-model = "newsDate" @on-change = "handleChange"></DatePicker>
		</div>
		<div id="map">
			<div id="pie">
			
			</div>

			<div id="bar">
				
			</div>
		</div>
	</div>
</template>

<script type="text/javascript">
import { mainServer } from 'server/mainserver.js';
import { newsType } from 'server/en2ch.js';
import { DatePicker } from 'iview';
import echarts from 'echarts'
	export default {
		name : 'chart',
		data () {
			return {
				chart : '',
				pieData : [],//获取的数据[{type:''},{}]
				piechart : '',
				newsDate: ''// 新闻过滤的时间段
			}
		},
		components : {
			DatePicker
		},
		methods : {
			drawPie(id,data){
				let name = []
				data.forEach(item =>{
					name.push(item.name)
				})
				this.piechart = echarts.init(document.getElementById(id));
				this.piechart.setOption({
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
			},
			drawBar(id,data){
				let _this = this;
				let xdata = [];
				let ydata = []
				let objectkey = Object.keys(data).sort();
				objectkey.forEach(item => {
					xdata.push(item)
					ydata.push(data[item])
				})
				let chart = echarts.init(document.getElementById(id))
				chart.setOption({
					tooltip : {
						color : [],
				        trigger: 'axis',
				        formatter : function(a){
				        	return `${a[0].axisValueLabel}:搜集${a[0].value}条新闻`
				        },
				        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
				            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
				        }
				    },
				    xAxis: {
				        type: 'category',
				        data: xdata
				    },
				    yAxis: [
				    		{
				    			type : 'value'
				    		},
				    		{
				    			type : 'value',
				    			show : false
				    		}
				    		],
				    series: [
				    {
				        data: ydata,
				        type: 'bar'
				    },
				    {
				    	data : ydata,
				    	type : 'line'
				    }
				    ]
				})
				chart.on('click',params => {
					var time = params.name;
					mainServer.getNews({params : {type : 'time',time : time}}).then(res => {
						let pieData = _this.createData(res.data,'type')
						_this.pieData = []
						for (var key in pieData){
							if(newsType[key]){
								_this.pieData.push({name : newsType[key], value : pieData[key]})	
							}else{
								_this.pieData.push({name : key, value : pieData[key]})
							}
							
						}
						_this.piechart.dispose()
						_this.drawPie('pie',_this.pieData)
					})
				})
			},
			createData(arr,key){
				let tmp = {}
				let current = ''
				arr.forEach((item,i)=>{
					if(item[key] == current){
						if(current in tmp){
							tmp[current] += 1;
						}else{
							tmp[current] = 1;
						}
					}else{
						current = item[key];
						if(current in tmp){
							tmp[current] += 1;
						}else{
							tmp[current] = 1;
						}
					}
				})
				return tmp
			},
			handleChange(e) {
				this.newsDate = e;
				let time = e[0]+ '/' +e[1];
				mainServer.getNews({params:{type: 'date', time: time}}).then(res => {
					console.log(res);
				})
			}
		},
		mounted () {
			var _this = this;
			mainServer.getNews({params:{type:'chart'}}).then( res =>{
				let pieData = _this.createData(res.data,'type')
				let barData = _this.createData(res.data,'time')
				for (var key in pieData){
					if(newsType[key]){
						_this.pieData.push({name : newsType[key], value : pieData[key]})	
					}else{
						_this.pieData.push({name : key, value : pieData[key]})
					}
					
				}
				_this.drawBar('bar',barData)
				_this.drawPie('pie',_this.pieData)
			})
		}
	}
</script>

<style lang = "scss">
	@import './chart.scss'
</style>
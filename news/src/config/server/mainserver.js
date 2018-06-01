/*
* @Author: wangfpp
* @Date:   2018-04-25 15:24:23
* @Last Modified by:   wangfpp
* @Last Modified time: 2018-06-01 11:34:44
*/
import axios from 'axios'
axios.interceptors.response.use(response =>{
	return response
}, err => {
	status = err.response.status
	console.log(status)
	if(status == 401){
		window.location.href= 'http://0.0.0.0:8081/#/'
	}
	return Promise.reject(err)
})
let mainServer = {
	
}
const jsonPath = 'static/json/'
// if (process.env.NODE_ENV == 'development'){//匹配线上环境还是测试环境
// 	mainServer = {
// 		getNews : (params =>{
// 			return axios.get(`../../static/json/allNews.json`,params)
// 		}),
// 		controlNews : (params =>{
// 			return new Promise((resolve,reject)=>{
// 				axios.get(`/api/txt/control/`,params).then( res=>{
// 					resolve(res.data)
// 				},err =>{
// 					console.log(err)
// 				})
// 			})
// 		}),
// 	}
// }else{
	mainServer = {
		getNews :(params =>{//获取新闻列表
			return new Promise((resolve,reject)=>{
				axios.get(`/api/txt/`,params).then( res=>{
					resolve(res.data)
				}).catch(err =>{
					reject(err);
				})
			})
		}),
		controlNews : (params =>{//获取新闻详情
			return new Promise((resolve,reject)=>{
				axios.get(`/api/txtdetail/`,params).then( res=>{
					resolve(res.data)
				}).catch(err =>{
					reject(err);
				})
			})
		}),
		updateNews : (params =>{//更新新闻
			return new Promise((resolve,reject)=>{
				axios.put(`/api/txtdetail/`,params).then( res=>{
					resolve(res.data)
				}).catch(err =>{
					reject(err);
				})
			})
		}),
		register : (params => {//注册
			return new Promise( (resolve,reject) => {
				axios.post(`/api/register/`,params).then( res =>{
					resolve(res.data)
				}).catch(err =>{
					reject(err);
				})
			})
		}),
		login : params => {//登录
			return new Promise( (resolve,reject) => {
				axios.post(`/api/login/`,params).then( res => {
					resolve(res.data)
				}).catch(err =>{
					reject(err);
				})
			})
		},
		prelogin : params => {
			return new Promise( (resolve, reject) => {
				axios.get(`/api/prelogin/`,params).then( res => {
					resolve(res.data)
				}).catch(err =>{
					reject(err);
				})
			})
		},
		getOriginalNews : params => {
			return new Promise((resolve,reject)=>{
				axios.get(`https://bird.ioliu.cn/v1?url=${params}`).then(res => {
						resolve(res.data)
				})
			})
		}
	}
export {mainServer}











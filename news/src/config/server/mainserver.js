/*
* @Author: wangfpp
* @Date:   2018-04-25 15:24:23
* @Last Modified by:   wangjb
* @Last Modified time: 2018-05-06 00:07:00
*/
import axios from 'axios'
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
		getNews :(params =>{
			return new Promise((resolve,reject)=>{
				axios.get(`/api/txt/`,params).then( res=>{
					resolve(res.data)
				}).catch(err =>{
					reject(err);
				})
			})
		}),
		controlNews : (params =>{
			return new Promise((resolve,reject)=>{
				axios.get(`/api/txtdetail/`,params).then( res=>{
					resolve(res.data)
				}).catch(err =>{
					reject(err);
				})
			})
		}),
		updateNews : (params =>{
			return new Promise((resolve,reject)=>{
				axios.put(`/api/txtdetail/`,params).then( res=>{
					resolve(res.data)
				}).catch(err =>{
					reject(err);
				})
			})
		}),
		register : (params => {
			return new Promise( (resolve,reject) => {
				axios.post(`/api/register/`,params).then( res =>{
					resolve(res.data)
				}).catch(err =>{
					reject(err);
				})
			})
		}),
		login : params => {
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











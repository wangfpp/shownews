/*
* @Author: wangfpp
* @Date:   2018-04-25 15:33:25
* @Last Modified by:   wangfpp
* @Last Modified time: 2018-04-25 15:44:10
*/
const location = window.location;
const Domain = {
	location : window.location,
	href : location.href,
	protocol : location.protocol,
	host : location.host,
	hostname : location.hostname,
	port : location.port,
	search : location.search,
	hash : location.hash
}
export {Domain}
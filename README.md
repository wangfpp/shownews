# shownews
# 项目背景：
- 把search_news获取到的新闻信息存到Mysql中
	- 后期迁徙MongoDB
- 新闻信息的可视化(前端展示/更新)
- 利用Tornado来做以上两者的桥梁

# 后端实现
## 1.项目依赖:
- Python2.7
- Mysql
- Tornado
- json
	- 格式化JSON数据
- binascii
	- 对获取到的txt内容编码存储

# 前端实现
## 1.项目依赖:
- Vue 2.5.2
- Webpack 3.6.0
- Axios 0.18.0
- 项目具体内容请看news文件目录

# 具体功能
- 新闻存储到数据库
	- 数据库名称: news 
	- 数据表:
		- newsInfo 所有的新闻信息(id name type text size time)
		- user 用户信息(phonenum name password)
- 注册 登录功能
- 获取所有新闻
- 更新/更改新闻信息

# 有待优化项
- 界面优化
- 登录注册的用户密码加密
- 文档的整理
- 数据库的迁徙

# 项目展示
![登录页](./login.png)
![主页]('./main.png')

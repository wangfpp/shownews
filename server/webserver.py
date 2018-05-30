# -*- coding: utf-8 -*-
# @Author: wangfpp 
# @Date: 2018-04-23 10:16:10 
# @Last Modified by:   wangfpp
# @Last Modified time: 2018-05-30 22:27:17
import tornado.ioloop
import tornado.web
import torndb
import json
import binascii
import numpy
import base64
db = torndb.Connection(host = "localhost", database = "news", user = "root", password = "ddkk1212")

class BaseHandler(tornado.web.RequestHandler):#获取用户信息  需要挂载一个login_url
    def get_current_user(self):
        phonenum = self.get_secure_cookie('news')
        return phonenum

class mainHandler(BaseHandler):#获取新闻信息接口
    def get(self,body):
        query =  self.request.arguments
        
        if query:
            getType = query['type'][0]
            if getType == 'page':
                page = int(query['page'][0])
                size = int(query['size'][0])
                info = db.query("select * from newsInfo;")
                total = len(info)
                info = info[(page -1)*size:(page)*size]
                for item in info:
                    item['text'] = binascii.unhexlify(item['text']) 
            elif getType == 'chart':
                info = db.query("select type from newsInfo")
                total = len(info)
        else:
            info = db.query("select * from newsInfo;")
            total = len(info)
            for item in info:
                item['text'] = binascii.unhexlify(item['text']) 
        #jret = json.dumps(info)
        
        self.set_header('Access-Control-Allow-Origin','*')
        self.finish(json.dumps({'data':info,'total':total}))
        #self.write(info)
class controlNews(tornado.web.RequestHandler):#获取新闻信息的详细信息 以及更新新闻信息
    def get(self,database):
        newsid =  str('"'+self.get_query_arguments('id',strip=True)[0]+'"')
        sql = "select * from newsInfo where id={0}".format(newsid)
        newsDetail = db.query(sql)
        for item in newsDetail:
            item['text'] = binascii.unhexlify(item['text'])
        self.finish(json.dumps(newsDetail))
    def put(self,text):
        news = json.loads(self.request.body)
        if news:
            newsid = news['id']
            text = binascii.hexlify(news['text'].encode('utf-8'))
            sql = "update newsInfo set text='"'%s'"' where id='"'%s'"';"%(text,newsid)
            db.execute(sql)
        else:
            self.set_status(500)
        
class register(tornado.web.RequestHandler):#注册
    def post(self,user):
        userinfo = json.loads(self.request.body)
        print userinfo
        if userinfo:
            phonenum = userinfo['phonenum']
            userName = userinfo['username']
            passWord = userinfo['password']
            search =  db.query("select * from user;")
            if self.isexit(phonenum,search):
                self.set_status(500)
                self.finish(json.dumps({"reason":'user is exit'}))
            else:
                sql = "insert into user(phonenum,name,password) values('"'%s'"','"'%s'"','"'%s'"')"%(phonenum,userName,passWord)
                try:
                    db.execute(sql)
                    self.set_status(500)
                    self.finish(json.dumps({"data":'failed'}))
                except:
                    self.set_status(200)
                    self.finish(json.dumps({"data":'sucess'}))
        else:
            self.set_status(400)
    def isexit(self,num,arr):
        for item in arr:
            if item['phonenum'] == num:
                return True
                break
        return False
class login(tornado.web.RequestHandler):#登录
    def post(self,username):
        userinfo = json.loads(self.request.body)
        if userinfo:
            phonenum = userinfo['phonenum']
            password = userinfo['password']
            sql = "select * from user where phonenum='"'%s'"';"%(phonenum)
            search =  db.query(sql)
            if len(search) == 0:
                self.set_status(403)
                self.set_header('Access-Control-Expose-Headers','Authentication')
                self.finish(json.dumps({"reason":'user not exit'}))
            else :
                if search[0]['password'] == password:
                    global user
                    user = phonenum
                    self.set_status(200)
                    self.set_secure_cookie('news',phonenum,expires_days=1,version=None)
                    self.finish(json.dumps({"data":{"username":search[0]['name'],"phonenum":search[0]['phonenum']}}))
                else:
                    self.set_status(403)
                    self.finish(json.dumps({"reason":'pass err'}))
        else:
            self.set_status(400)
class author(BaseHandler):#用户认证
    @tornado.web.authenticated
    def get(self):
        cookie = self.get_secure_cookie('news')
        name = self.get_current_user()
        print 'aaa{}'.format(name)
        # if cookie:
        #     self.set_status(200)
        #     self.finish({'data':'success'})
class houses(tornado.web.RequestHandler):
    def get(self,body):
        query =  self.request.arguments
        data = [{'id':'aaaaa','titile':'河南庄北校区','location':'5楼','price':'500.00','des':['学区房','商业区','海景房']},
                {'id':'bbbb','titile':'河南庄北校区','location':'5楼','price':'500.00','des':['学区房','商业区','海景房']},
               {'id':'ccc','titile':'河南庄北校区','location':'5楼','price':'500.00','des':['学区房','商业区','海景房']},
                {'id':'ddd','titile':'河南庄北校区','location':'5楼','price':'500.00','des':['学区房','商业区','海景房']}]
        if query:
            idx = query['id'][0]
            data_body = []
            for item in data:
                print item['id'] == idx
                if item['id'] == idx:
                    data_body = item
                    break
            self.finish(json.dumps({'data':data_body}))
        else:
            self.finish(json.dumps({'data':data}))
class img(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-type", "image/png")
        f = open('../login.png','rb')
        img = f.read()
        f.close()
        #self.finish({'img':base64.b64encode(img)})
        self.write('data:image/png;base64,{}'.format(base64.b64encode(img)))
                      

def main():
    settings = {
        "cookie_secret": "aaaaa",
        "login_url": "/api/prelogin/",
    }
    app = tornado.web.Application(
        [(r'/api/txt/(.*)',mainHandler),
        (r'/api/txtdetail/(.*)',controlNews),
        (r'/api/register/(.*)',register),
        (r'/api/login/(.*)',login),
        (r'/api/prelogin/',author),
        (r'/api/houses/(.*)',houses),
        (r'/api/img/',img)
        ],**settings
    )
    app.listen('8080')
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
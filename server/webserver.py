# -*- coding: utf-8 -*-
# @Author: wangfpp 
# @Date: 2018-04-23 10:16:10 
# @Last Modified by:   wangjb
# @Last Modified time: 2018-05-02 17:27:01
import tornado.ioloop
import tornado.web
import torndb
import json
import binascii
import numpy
db = torndb.Connection(host = "localhost", database = "news", user = "root", password = "ddkk1212")

class mainHandler(tornado.web.RequestHandler):
    def get(self,body):
        query =  self.request.arguments
        print query
        if query:
            page = int(query['page'][0])
            size = int(query['size'][0])
            info = db.query("select * from newsInfo;")
            total = len(info)
            info = info[(page -1)*size:(page)*size]
            print len(info)
        else:
            info = db.query("select * from newsInfo;")
            total = len(info)
        #jret = json.dumps(info)
        for item in info:
            item['text'] = binascii.unhexlify(item['text']) 
        self.set_header('Access-Control-Allow-Origin','*')
        self.finish(json.dumps({'data':info,'total':total}))
        #self.write(info)
class controlNews(tornado.web.RequestHandler):
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
        
class register(tornado.web.RequestHandler):
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
class login(tornado.web.RequestHandler):
    def post(self,user):
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
                    self.set_status(200)
                    self.set_secure_cookie('news','aaaaaa',expires_days=1,version=None)
                    self.finish(json.dumps({"data":{"username":search[0]['name']}}))
                else:
                    self.set_status(403)
                    self.finish(json.dumps({"reason":'pass err'}))
        else:
            self.set_status(400)
class author(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie('news')
        if cookie:
            self.set_status(200)
            self.finish({'data':'success'})
def main():
    app = tornado.web.Application(
        [(r'/api/txt/(.*)',mainHandler),
        (r'/api/txtdetail/(.*)',controlNews),
        (r'/api/register/(.*)',register),
        (r'/api/login/(.*)',login),
        (r'/api/prelogin/',author)
        ],cookie_secret="aaaaaa"
    )
    app.listen('8080')
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
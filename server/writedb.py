# -*- coding: utf-8 -*-
# @Author: wangfpp 
# @Date: 2018-04-13 10:26:35 
# @Last Modified by:   wangfpp 
# @Last Modified time: 2018-04-13 10:26:35 
import torndb
import os,sys
import re
import hashlib
import binascii


curr_path = os.path.dirname(os.path.abspath(__file__))
comm_path = os.path.dirname(curr_path)
if comm_path not in sys.path:
    sys.path.append(comm_path)
class writedb():
    def init(self):
        pass
    def readtxt(self,full_path):
        with open(full_path,'rb') as f:  
            txt = binascii.hexlify(f.read())
            name = os.path.basename(full_path)
            size = self.formSize(os.path.getsize(full_path))
            idx = str(hashlib.md5(name).hexdigest())
            index = (re.search('_',name).span())
            typex = name[0:index[0]]
            patten = re.compile(r'\d{4}_\d{2}-\d{2}')
            date = patten.findall(name)[0].replace('_','-')
           # return idx,name,typex,txt,size,date
        db = self.conn_db()
        sql ='insert into newsInfo (id,name,type,text,size,time) values ("' + idx +'","' + name +'","' +typex+'","'+ txt + '","'+size+'","'+date+'");'
        db.execute(sql)
    def formSize(self,bytes):
        try:
            bytes = float(bytes)
            kb = bytes/1024
        except:
            print ('err')
            return 'ERROR'
        if kb >= 1024:
            M = kb / 1024
            if M >= 1024:
                G = M/1024
                return '%fG' % (G)
            else:
                return "%fM" % (M) 
        else:
            return "%.2fkb" % (kb)
    def getAllTxt(self,folder):
        folder_list =  os.listdir(folder)
        for item in folder_list:
            self.readtxt(folder+'/'+item)
    def conn_db(self):
        try:
            database = "news"
            db = torndb.Connection(host = "localhost",database = database, user = "root", password = "ddkk1212")
            print '数据库 {0} 连接成功'.format(database)
            return db
        except:
            print "数据库链接失败"
        #self.readtxt(curr_path + '/txt/business_2018_02-08_8444119.txt')
        # sql ='select * from form;'
        # data = db.execute(sql)
        #print data
        
        
if __name__ == '__main__':
    a = writedb()
    #a.conn_db()
    #a.readtxt(curr_path + '/txt/sh_2018_02-06_8442753.txt')
    a.getAllTxt(curr_path+'/txt')
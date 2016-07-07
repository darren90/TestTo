#-*- coding: UTF-8 -*-

import  MySQLdb
import hashlib


def get_conn():
    host = "127.0.0.1"
    port = 3306
    db = "fei"
    user = "root"
    password = "root"
    conn = MySQLdb.connect(host = host,
                           user = user,
                           passwd = password,
                           db = db,
                           port = port,
                           charset = "utf8")
    return conn

# 爬取的地址
class Spiderdb(object):
    def __init__(self, url,md5,content):
        self.url = url
        self.md5 = md5
        self.content = content

    @staticmethod
    def saveSpider(url,content):
        md5_ = hashlib.md5(content.encode('utf-8')).hexdigest()

        conn = get_conn()
        cursor = conn.cursor()
        sql = "INSERT into spiderdb (url,md5,stype) values (\'%s\' ,\'%s\' ,\'%s\')" % (url,md5_,'carCalBeatiful')
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    # 终极检验，url+md5
    @staticmethod
    def isThisHadSpider(url,content):
        md5 = hashlib.md5(content.encode('utf-8')).hexdigest()
        # print 'url:%s,md5,,%s' % (url, md5)

        conn = get_conn()
        cursor = conn.cursor()
        sql = "select * from spiderdb where md5 = \'%s\' or url = \'%s\' ;" % (md5,url)
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = False
        if len(rows) != 0:
            result = True
        conn.commit()
        cursor.close()
        conn.close()
        return result  

    @staticmethod
    def query_all():
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT * from spiderdb"
        cursor.execute(sql)
        rows = cursor.fetchall()
        spiderdbs = []
        for row in rows:
            spiderdb = Spiderdb(row[0],row[1])
            spiderdbs.append(spiderdb)
        conn.commit()
        cursor.close()
        conn.close()
        return spiderdbs        
       

# CalBeatiful
class User(object):
    def __init__(self,title,detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url):
        self.title = title
        self.detail_url = detail_url
        self.icon_url = icon_url
        self.bbs_id = bbs_id
        self.bbs_name = bbs_name
        self.sub_title = sub_title
        self.bbs_url = bbs_url

    def save(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql_sel = "select * from CalBeatiful where title = \'%s\' and detail_url = \'%s\' ;" % (self.title,self.detail_url)
        cursor.execute(sql_sel)
        rows = cursor.fetchall()
        # 判断是否已经储存过
        if len(rows) != 0:
            # print '---YES--这个内容已经爬取--'
            return
        sql = "INSERT into CalBeatiful (title,detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url) values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(self.title,self.detail_url,self.icon_url,self.bbs_id,self.bbs_name,self.sub_title,self.bbs_url))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def query_all():
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT * from CalBeatiful"
        cursor.execute(sql)
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = User(row[0],row[1])
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
        return users

    def __str__(self):
        return "id:{}-name:{}".format(self.title,self.detail_url)
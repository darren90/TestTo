#-*- coding: UTF-8 -*-

import  MySQLdb
import hashlib
# 导入SQLite驱动:
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_conn():

    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('rank.db')

    cursor = conn.cursor()
    cursor.execute('create table if NOT EXISTS rank_word (id INTEGER primary key AUTOINCREMENT, rank_year varchar(200), rank varchar(200), last_rank varchar(200), co_name varchar(200),co_detailurl varchar(200), income varchar(200), profit varchar(200), nation varchar(200))')

    cursor.close()
    conn.commit()

    return conn

# 爬取的地址
class Spiderdb(object):
    def __init__(self, url,md5,content):
        self.url = url
        self.md5 = md5
        self.content = content

    # 抓取 品牌
    @staticmethod
    def save_sbrand(url,content):
        md5_ = hashlib.md5(content.encode('utf-8')).hexdigest()

        conn = get_conn()
        cursor = conn.cursor()
        sql = "INSERT into spiderdb (url,md5,stype) values (\'%s\' ,\'%s\' ,\'%s\')" % (url,md5_,'sbrand')

        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    #  是否品牌页面已经抓取了
    @staticmethod
    def is_sbrand_HadSpider(url,content):
        md5 = hashlib.md5(content.encode('utf-8')).hexdigest()

        conn = get_conn()
        cursor = conn.cursor()
        sql = "select * from spiderdb where stype = 'sbrand' and ( url = \'%s\' or md5 = \'%s\');" % (url,md5)

        cursor.execute(sql)
        rows = cursor.fetchall()
        # print '--11--'
        # print rows
        result = False
        if len(rows) != 0:
            result = True
        conn.commit()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def save_carvideo_spider(url,content):
        md5_ = hashlib.md5(content.encode('utf-8')).hexdigest()

        conn = get_conn()
        cursor = conn.cursor()
        sql = "INSERT into spiderdb (url,md5,stype) values (\'%s\' ,\'%s\' ,\'%s\')" % (url,md5_,'carvideo')

        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    # 终极检验，url+md5
    @staticmethod
    def is_carvideo_HadSpider(url,content):
        md5 = hashlib.md5(content.encode('utf-8')).hexdigest()

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

# Auto_Brand
class Auto_Brand(object):
    def __init__(self,brand_name,brand_url,brand_imgurl,sbrand_name,car_name,car_url):
        self.brand_name = brand_name
        self.brand_url = brand_url
        self.brand_imgurl = brand_imgurl
        self.sbrand_name = sbrand_name
        self.car_name = car_name
        self.car_url = car_url

    def save(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql_sel = "select * from auto_brand where sbrand_name = \'%s\' and car_name = \'%s\' ;" % (self.sbrand_name,self.car_name)
        cursor.execute(sql_sel)
        rows = cursor.fetchall()
        # 判断是否已经储存过
        if len(rows) != 0:
            print '---YES--这个内容已经爬取--'
            return
        sql = "INSERT into auto_brand (brand_name,brand_url,brand_imgurl,sbrand_name,car_name,car_url) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(self.brand_name,self.brand_url,self.brand_imgurl,self.sbrand_name,self.car_name,self.car_url))
        conn.commit()
        cursor.close()
        conn.close()

# car_videos
class Rank_Word(object):
    def __init__(self, rank_year , rank , last_rank , co_name,co_detailurl , income , profit , nation):
        self.rank_year = rank_year
        self.rank = rank
        self.last_rank = last_rank
        self.co_name = co_name
        self.co_detailurl = co_detailurl
        self.income = income
        self.profit = profit
        self.nation = nation

    def save(self):
        conn = get_conn()
        cursor = conn.cursor()

        # sql_sel = "select * from rank_word where rank_year = \'%s\';" % (self.rank_year)
        # # print sql_sel
        # cursor.execute(sql_sel)
        # rows = cursor.fetchall()
        # # 判断是否已经储存过
        # if len(rows) != 0:
        #     print '---YES--这个内容已经爬取--'
        #     return
        sql = "INSERT into rank_word (rank_year , rank , last_rank , co_name,co_detailurl , income , profit , nation) values (%s,%s,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" % (
        self.rank_year, self.rank, self.last_rank, self.co_name,self.co_detailurl, self.income, self.profit,self.nation)
        print '%s ;'% sql
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def __str__(self):
        return "id:{}-name:{}".format(self.car_name,self.video_play_url)
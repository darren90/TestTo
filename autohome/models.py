#-*- coding: UTF-8 -*-

# from app import db
import  MySQLdb

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

class User(object):

    def __init__(self,user_id,user_name):
        self.user_id = user_id
        self.user_name = user_name

    def save(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "INSERT into user (user_id,user_name) values (%s,%s)"
        cursor.execute(sql, (self.user_id, self.user_name))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def query_all():
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT * from user"
        cursor.execute(sql)
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = User(row[0], row[1])
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
        return users

    @staticmethod
    def query(page,count):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT * from user LIMIT %s,%s" % (page,count)
        cursor.execute(sql)
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = User(row[0], row[1])
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
        return users


    def to_json(self):
        return {
            'user_id':str(self.user_id),
            'user_name':self.user_name
        }


class CalBeatiful(object):
    def __init__(self, title, detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url):
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
        sql = "INSERT into CalBeatiful (user_id,user_name) values (%s,%s)"
        cursor.execute(sql, (self.user_id, self.user_name))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def query_all():
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT title, detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url from CalBeatiful"
        cursor.execute(sql)
        rows = cursor.fetchall()
        carbs = []
        for row in rows:
            carb = CalBeatiful(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            carbs.append(carb)
        conn.commit()
        cursor.close()
        conn.close()
        return carbs

    @staticmethod
    def query(page, count):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT title, detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url from CalBeatiful LIMIT %s,%s" % (page, count)
        cursor.execute(sql)
        rows = cursor.fetchall()
        carbs = []
        for row in rows:
            carb = CalBeatiful(row[0], row[1],row[2], row[3],row[4], row[5],row[6])
            carbs.append(carb)
        conn.commit()
        cursor.close()
        conn.close()
        return carbs

    @staticmethod
    def title_search(keyword):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT title, detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url from CalBeatiful where title like \'%%%s%%\' " % (keyword)

        cursor.execute(sql)
        rows = cursor.fetchall()
        carbs = []
        for row in rows:
            carb = CalBeatiful(row[0], row[1],row[2], row[3],row[4], row[5],row[6])
            carbs.append(carb)
        conn.commit()
        cursor.close()
        conn.close()
        return carbs

    @staticmethod
    def bbsname_search(keyword):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT title, detail_url,icon_url,bbs_id,bbs_name,sub_title,bbs_url from CalBeatiful where bbs_name like \'%%%s%%\' " % (keyword)

        cursor.execute(sql)
        rows = cursor.fetchall()
        carbs = []
        for row in rows:
            carb = CalBeatiful(row[0], row[1],row[2], row[3],row[4], row[5],row[6])
            carbs.append(carb)
        conn.commit()
        cursor.close()
        conn.close()
        return carbs

    def to_json(self):
        return {
            # 'user_id': str(self.user_id),
            # 'user_name': self.user_name
            'title':self.title,
            'detail_url':self.detail_url,
            'icon_url':self.icon_url,
            'bbs_id':self.bbs_id,
            'bbs_name':self.bbs_name,
            'sub_title':self.sub_title,
            'bbs_url':self.bbs_url
        }

# 搜索视频
class CarVideos(object):
    def __init__(self,car_name, car_level, car_video_url, video_title, video_imgurl, video_timel,video_play_url):
        self.car_name = car_name
        self.car_level = car_level
        self.car_video_url = car_video_url
        self.video_title = video_title
        self.video_imgurl = video_imgurl
        self.video_timel = video_timel
        self.video_play_url = video_play_url

    @staticmethod
    def query_all():
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT car_name, car_level, car_video_url, video_title, video_imgurl, video_timel,video_play_url from car_videos"
        cursor.execute(sql)
        rows = cursor.fetchall()
        carcideos = []
        for row in rows:
            carvideo = CarVideos(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            carcideos.append(carvideo)
        conn.commit()
        cursor.close()
        conn.close()
        return carcideos

    @staticmethod
    def query(page, count):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT car_name, car_level, car_video_url, video_title, video_imgurl, video_timel,video_play_url from car_videos LIMIT %s,%s" % (page, count)
        cursor.execute(sql)
        rows = cursor.fetchall()
        carvideos = []
        for row in rows:
            carvideo = CarVideos(row[0], row[1],row[2], row[3],row[4], row[5],row[6])
            carvideos.append(carvideo)
        conn.commit()
        cursor.close()
        conn.close()
        return carvideos

    @staticmethod
    def car_name_search(keyword):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "SELECT car_name, car_level, car_video_url, video_title, video_imgurl, video_timel,video_play_url from car_videos where video_play_url !='' and car_name like \'%%%s%%\' " % (keyword)

        cursor.execute(sql)
        rows = cursor.fetchall()
        carvideos = []
        for row in rows:
            carvideo = CarVideos(row[0], row[1],row[2], row[3],row[4], row[5],row[6])
            carvideos.append(carvideo)
        conn.commit()
        cursor.close()
        conn.close()
        return carvideos


    def to_json(self):
        return {
            'car_name':self.car_name,
            'car_video_url':self.car_video_url,
            'video_title':self.video_title,
            'video_imgurl':self.video_imgurl,
            'video_timel':self.video_timel,
            'video_play_url':self.video_play_url
        }


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


    # def getCarbs(rows):
    #     carbs = []
    #     for row in rows:
    #         carb = CalBeatiful(row[0], row[1],row[2], row[3],row[4], row[5],row[6])
    #         carbs.append(carb)
    #     return carbs



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
            print  row
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





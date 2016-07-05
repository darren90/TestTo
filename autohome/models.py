from app import db
import  MySQLdb

class User(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String)



    def __init__(self,user_id,user_name):
        self.user_id = user_id
        self.user_name = user_name

    def to_json(self):
        return {
            'user_id':str(self.user_id),
            'user_name':self.user_name
        }
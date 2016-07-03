from app import db
import  MySQLdb

# class Todo(db.Model):
#     content = db.Column(db.String)
#     time = db.Column(db.String)
#     status = db.Column(db.Boolean)
#
#     def __init__(self,content,time):
#         self.content = content
#         self.time = time
#
#
#     def to_json(self):]
#         return {
#             'id': str(self.id),
#             'content': self.content,
#             'time': self.time,
#             'status': self.status
#         }


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
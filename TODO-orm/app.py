from flask.ext.sqlalchemy import  SQLAlchemy
from  flask import Flask,render_template,request,jsonify
# from models import  *
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@127.0.0.1:3306/fei"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return  render_template("index.html")

@app.route('/test')
def test():
    return "Hello da feige"

@app.route('/add',methods=['POST'])
def add():
    # form = request.form
    # content = form.get('content')
    # todo = Todo(content,"1231")
    # db.session.add(todo)
    # return jsonify(status="success")

    form = request.form
    content = form.get('content')
    print 'content:%s'%content
    id = form.get('id')
    user = User(id,content)
    db.session.add(user)
    db.session.commit()
    return jsonify(status="success")

@app.route('/delte/<string:todo_id>')
def delete(todo_id):
    pass


@app.route('/update',methods=['POST'])
def update():
    pass


@app.route('/list')
def list():
    users = User.query.all()
    return  jsonify(status="success",users=[user.to_json() for user in users])


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


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=8080)

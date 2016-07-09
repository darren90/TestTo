#-*- coding: UTF-8 -*-
from  flask import Flask,render_template,request,jsonify
from models import  *
app = Flask(__name__)

@app.route('/')
def index():
    return  render_template("index.html")

@app.route('/test')
def test():
    return "Hello da feige"

# @app.route('/add',methods=['POST'])
# def add():
#     form = request.form
#     content = form.get('content')
#     id = form.get('id')
#     user = User(id,content)
#     user.save()
#     return jsonify(status="success")

@app.route('/delte/<string:todo_id>')
def delete(todo_id):
    pass

@app.route('/update',methods=['POST'])
def update():
    pass


@app.route('/all')
def list():
    carbs = CalBeatiful.query_all()
    return  jsonify(status="success",users=[carb.to_json() for carb in carbs])

@app.route('/query/<page>/<count>')
def query(page,count):
    carbs = CalBeatiful.query(page,count)
    return  jsonify(status="success",users=[carb.to_json() for carb in carbs])

#搜索 - 标题
@app.route('/title/search/<keyword>/')
def title_search(keyword):
    carbs = CalBeatiful.title_search(keyword)
    return  jsonify(status="success",users=[carb.to_json() for carb in carbs])

#搜索 - bbs的名字
@app.route('/bbsname/search/<keyword>/')
def bbsname_search(keyword):
    carbs = CalBeatiful.bbsname_search(keyword)
    return  jsonify(status="success",users=[carb.to_json() for carb in carbs])


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=8080)

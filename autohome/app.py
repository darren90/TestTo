#-*- coding: UTF-8 -*-
from  flask import Flask,flash,render_template,request,jsonify,abort
from models import *
# from CarModel


app = Flask(__name__)
app.secret_key = 'dafeige'

# @app.route('/')
# def index():
#     return  render_template("index_1.html")

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


@app.route('/')
def index():
    return  render_template("index_1.html")

@app.route('/video')
def video_index():
    return  render_template("index.html")


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


#
#  汽车测评视频的搜索
#
@app.route('/car/query/<page>/<count>')
def query_carvideo(page,count):
    carvs = CarVideos.query(page,count)
    return  jsonify(status="success",users=[carv.to_json() for carv in carvs])

#搜索 - 标题
@app.route('/car/carname/search/<keyword>/')
def car_name_search(keyword):
    carvs = CarVideos.car_name_search(keyword)
    return  jsonify(status="success",users=[carv.to_json() for carv in carvs])

# 网页展示
@app.route('/search_video', methods=['POST'])
def search_video__():
    form = request.form
    keyword = form.get('content')
    if not keyword:
        abort(404)
    # if form.validate():
    #     content = form.content.data
    #     todo = Todo(content=content,time=datetime.now())
    #     todo.save()
    # todos = Todo.objects.order_by('-time')
    carvs = CarVideos.car_name_search(keyword)
    return render_template("index.html",videos=carvs)

@app.errorhandler(404)
def not_found(error):
    return  jsonify(status='error')#render_template('404.html')

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=8080)

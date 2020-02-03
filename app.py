from flask import Flask ,render_template
from data import Articles
from flask_mysqldb import MySQL
import pymysql

app = Flask(__name__)   #port 자동 지정으로 실행=>5000port
app.debug = True

Articles=Articles()
print(Articles)

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='myflaskapp', charset='utf8')
cursor = db.cursor()

cursor = db.cursor()

data1 = cursor.execute('INSERT INTO users(name,email,username,password) VALUES("kim","1@naver.com","modu","1234")')
print(data1)
# app.config['MySQL_HOST']='localhost'
# app.config['MySQL_USER']='root'
# app.config['MySQL_PASSWORD']='1234'
# app.config['MySQL_DB']='myflaskapp'
# app.config['MySQL_CURSORCLASS']='DictCursor'

# mysql=MySQL(app)
# cur = mysql.com

@app.route('/') # @=decorate, flask 안에 route라는 method존재 => 경로를 따라 실행 시킴
def hello():
    return render_template('home.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', data=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html', id=int(id), articles=Articles)

if __name__=='__main__':
    app.run(debug=True)

# if __name__=='__main__':   # __str__ =>이런식으로 쓰면 단독, 직접 실행은 되지만 import시 실행X
#     app.run(debug=True)  # 개발시에는 항상 debug mode 를 on(True)으로 해두어야 한다 off(False)
# debug mode on하는 다른 방식
#  app.debug = True
#  if __name__=='__main__':
#      app.run()



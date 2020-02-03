from flask import Flask ,render_template
from data import Articles

app = Flask(__name__)   #port 자동 지정=>5000port

app.debug = True

Articles=Articles()
print(Articles)

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

if __name__=='__main__':
    app.run(debug=True)

# if __name__=='__main__':   # __str__ =>이런식으로 쓰면 단독, 직접 실행은 되지만 import시 실행X
#     app.run(debug=True)  # 개발시에는 항상 debug mode 를 on(True)으로 해두어야 한다 off(False)
# debug mode on하는 다른 방식
#  app.debug = True
#  if __name__=='__main__':
#      app.run()



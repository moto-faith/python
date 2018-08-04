from flask import request
from flask import Flask
from flask import render_template
from spiderData import search_info

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('/search.html')

@app.route('/search')
def search():
    keyword = request.args.get('wd')
    result = search_info(keyword)
    return render_template('/result.html',data = result,num = len(result))


@app.route('/hello/<a>/<b>')
def hello(a,b):
    return render_template('hello.html',a=a,b=b)


if __name__ == '__main__':
    app.run()

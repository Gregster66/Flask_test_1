from flask import Flask,request
import re

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    args = request.args.get('search')
    with open('config.txt','r') as config:
        data  =config.read()

    return args


if __name__ == '__main__':
    app.run()

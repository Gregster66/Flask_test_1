from flask import Flask,request
from file_ingest import load_config

app = Flask(__name__)

props_dict = load_config("props.txt")

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    args = request.args.get('search')

    return props_dict[args]


if __name__ == '__main__':
    app.run()

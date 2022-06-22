from flask import Flask,request
from file_ingest import load_config

app = Flask(__name__)

props_dict = load_config("props.txt")

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/fetch', methods=['POST'])
def fetch():
    text = request.form.get('text', None)
    user = request.form.get('user_name', None)
    print(user + ":" + text)
    return text + " = " + props_dict[text]

@app.route('/list', methods=['POST'])
def list():
    text = request.form.get('text', None)
    user = request.form.get('user_name', None)
    print(user + ":" + text)
    keys_list = props_dict.keys()
    list = ""
    for key in keys_list:
        list = list + " \t " + key
    return list

if __name__ == '__main__':
    app.run()

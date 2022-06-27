from flask import Flask,request
from file_ingest import load_config,request_breakdown
import logging


app = Flask(__name__)

logging.basicConfig(format='%(asctime)s %(message)s',filename='flask_log.log', level=logging.DEBUG)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/fetch', methods=['POST'])
def fetch():
    text,text_array,user = request_breakdown(request)
    print(user + ":" + text)

    logging.info( str(user) + ":" + str(text))
    # res = '{"blocks": [{"type": "header","text": {"type": "plain_text","text":"' + str(text) + ' = ' + str(re.findall('^(.+?)\n',props_dict[text])[0]) + '","emoji": true}},{"type": "section","text": {"type": "mrkdwn","text": "' + props_dict[text] + '"}}]}'
    return "*" + text + "* = " + props_dict[text]

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

#@app.route('/', methods=['POST'])

if __name__ == '__main__':
    # app.run()
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)
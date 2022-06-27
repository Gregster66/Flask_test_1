from flask import Flask,request
from file_ingest import load_config,request_breakdown
import logging


app = Flask(__name__)

stanza_object = load_config()
logging.basicConfig(format='%(asctime)s %(message)s',filename='flask_log.log', level=logging.DEBUG)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/fetch', methods=['POST'])
def fetch():
    text,text_array,user = request_breakdown(request)
    conf_file,stanza = text_array[0],text_array[1]
    print(user + ":" + text)
    logging.info( str(user) + ":" + str(text))
    # if conf_file not in stanza_object:
    #     return f"⚠️*Error*  ⚠\nI don't have the settings for the {conf_file} conf file"
    if stanza.lower() not in stanza_object[conf_file]:
        if stanza.upper() not in stanza_object[conf_file]:
            return f"⚠️*Error*  ⚠\nI can not find stanza *'{stanza}'* in the *{conf_file}* conf file"
        else:
            return "*" + stanza.upper() + "* = " + stanza_object[conf_file][stanza.upper()]
    else:
        return "*" + stanza.lower() + "* = " + stanza_object[conf_file][stanza.lower()]

@app.route('/list', methods=['POST'])
def list():
    text,text_array,user = request_breakdown(request)
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
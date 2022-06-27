from web_conf_pull import links

def load_config():
    import re
    stanza_object = {}
    for key in links:

        #open file
        conf_file = key + '.txt'
        with open(conf_file,'r') as config:
            data = config.read()

        #regex out 2 capture groups, the name of the stanza and the remaining multiple lines of it's description
        stanza = re.findall('^([A-Za-z_]+)\s=\s(.+?)(?=^[A-Za-z_]+\s=|\Z)',data,re.DOTALL | re.MULTILINE)

        #populate dictionary with each pair of regex groups, the stanza name being the key. The previous objects was a tuple. I am moving the data to a dictionary because it allows me to search based on KEY.
        conf_stanza = {}
        for row in stanza:
            conf_stanza[row[0]] = row[1]
        stanza_object[key] = conf_stanza

    return stanza_object

def request_breakdown(request):
    text = request.form.get('text', None)
    user = request.form.get('user_name', None)
    text_array = text.split(" ")
    return text, text_array, user


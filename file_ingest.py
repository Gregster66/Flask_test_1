def load_config(file):
    import re
    #open file
    with open(file,'r') as config:
        data = config.read()

    #regex out 2 capture groups, the name of the stanza and the remaining multiple lines of it's description
    stanza = re.findall('^([A-Za-z_]+)\s=\s(.+?)(?=^[A-Za-z_]+\s=|\Z)',data,re.DOTALL | re.MULTILINE)

    stanza_dict = {}
    #populate dictionary with each pair of regex groups, the stanza name being the key. The previous objects was a tuple. I am moving the data to a dictionary because it allows me to search based on KEY.
    for row in stanza:
        stanza_dict[row[0]] = row[1]

    return stanza_dict

def request_breakdown(request):
    text = request.form.get('text', None)
    user = request.form.get('user_name', None)
    text_array = text.split(" ")
    return text_array, user

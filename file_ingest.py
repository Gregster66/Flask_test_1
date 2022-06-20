def load_config():
    import re
    #open file
    with open('config.txt','r') as config:
        data = config.read()

    #regex out 2 capture groups, the name of the stanza and the remaining multiple lines of it's description
    stanza = re.findall('^([A-Za-z_]+)\s=\s(.+?)(?=^[A-Za-z_]+\s=|\Z)',data,re.DOTALL | re.MULTILINE)

    global props_dict
    props_dict = {}
    #populate dictionary with each pair of regex groups, the stanza name being the key
    for row in stanza:
        props_dict[row[0]] = row[1]

load_config()
#check for value in dictionary
if 'TRUNCATE' in props_dict:
    print("found it!")
else:
    print("missing")
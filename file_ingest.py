def load_config(file):
    import re
    #open file
    with open(file,'r') as config:
        data = config.read()

    #regex out 2 capture groups, the name of the stanza and the remaining multiple lines of it's description
    stanza = re.findall('^([A-Za-z_]+)\s=\s(.+?)(?=^[A-Za-z_]+\s=|\Z)',data,re.DOTALL | re.MULTILINE)

    props_dict = {}
    #populate dictionary with each pair of regex groups, the stanza name being the key. The previous objects was a tuple. I am moving the data to a dictionary because it allows me to search based on KEY.
    for row in stanza:
        props_dict[row[0]] = row[1]

    return props_dict

# load_config('props.txt')
# #check for value in dictionary
# if 'TRUNCATE' in props_dict:
#     print("found it!")
# else:
#     print("missing")
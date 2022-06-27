#Pulling data from the Splunk Docs web pages and saving them into files
import requests
from bs4 import BeautifulSoup

links = {'props': 'https://docs.splunk.com/Documentation/Splunk/9.0.0/admin/Propsconf',
         'transforms': 'https://docs.splunk.com/Documentation/Splunk/9.0.0/admin/Transformsconf',
         'inputs': 'https://docs.splunk.com/Documentation/Splunk/9.0.0/admin/Inputsconf'}

def web_pull(conf):
    #check if the correct key conf file type was selected
    if conf in links:
        web_request = requests.get(links[conf])
        soup = BeautifulSoup(web_request.text, 'html.parser')
        sections = []
        for section in soup.find_all('pre'):
            sections.append(section.text)
        file = conf + '.txt'
        f = open(file, "w")
        for sec in sections:
            f.write(sec)
        f.close()

    else:
        raise Exception("Incorrect conf file specified")


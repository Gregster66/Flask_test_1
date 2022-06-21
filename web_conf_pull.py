#Pulling data from the Splunk Docs web pages and saving them into files
import requests
from bs4 import BeautifulSoup

links = {'props': 'https://docs.splunk.com/Documentation/ITSI/latest/Configure/props.conf',
         'transforms': 'https://docs.splunk.com/Documentation/ITSI/latest/Configure/transforms.conf'}

web_request = requests.get(links['props'])
soup = BeautifulSoup(web_request.text,'html.parser')

sections = []
for section in soup.find_all('pre'):
    sections.append(section.text)

f = open('props.txt', "w")
for sec in sections:
    f.write(sec)
f.close()

#Pulling data from the Splunk Docs web pages and saving them into files
import requests
from bs4 import BeautifulSoup

links = {'props': 'https://docs.splunk.com/Documentation/ITSI/latest/Configure/props.conf',
         'transforms': 'https://docs.splunk.com/Documentation/ITSI/latest/Configure/transforms.conf'}

web_request = requests.get(links['props'])
soup = BeautifulSoup(web_request.text,'html.parser')

sections = []
titles = []
for section in soup.find_all('pre'):
    sections.append(section.text)
for title in soup.find_all('h3', class_='mw-headline'):
    titles.append(title.text)

# titles.insert(0,'Overview')

for a in titles:
    print(a)

# section_dict = {}
# section_dict['Overview'] = sections[0].text
# for x in len(sections):
#     section_dict[titles[x].text] = sections[x + 1].text
#
# print(section_dict)
#


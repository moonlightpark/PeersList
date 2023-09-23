'''
Find all nodes,
crawl the node miner address,
and save it as a file.
'''
import pprint
import pandas as pd
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('http://main.saseul.net/peer')
bsObject = BeautifulSoup(url, "html.parser")

f = open('./peer_original_data.txt', 'w')
f.write(str(bsObject))
f.close()

file = open('./peer_original_data.txt')
js = json.load(file)
res = json.dumps(js)
file.close()

text = pprint.pformat(json.loads(res))
#f = open('./peers.json', 'w')
#f.write(str(text))
#f.close()

#
###########################
#
file_path = './peers.json'
with open(file_path,encoding='UTF-8') as json_file:
    data = json.load(json_file)
    print(type(data))



f = open('./miner_address.txt', 'w')

for i in data['peers']:
    print(data['peers'][i]['address'])
    line = data['peers'][i]['address']+'\n'
    f.write(line)

f.close()
'''
전체 노드를 찾아서 노드 보상 주소를 크롤링 한 후, 파일로 저장
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

for i in data['peers']:
    print(data['peers'][i]['address'])

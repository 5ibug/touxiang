#coding:utf-8
import requests
import re
import urllib
import urllib.request
import time
import random

file_path='E:/touxiang/'
temp = 0
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
def downimg(url):
    urllib.request.urlretrieve(url, file_path + str(round(time.time())) + str(random.randint(11111111111, 999999999999)) +".png") 
    print(url+'下载完成\n')

while(True):
    html = requests.get("https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum%2Creply_count&filter_id=%E5%A4%B4%E5%83%8F&start="+str(temp))
    html = html.json()['data']['object_list']
    for json2 in html:
        downimg(re.sub('\[\'(.*?)\'\]', r'\1', str(json2['album']['covers'])))
        downimg(json2['photo']['path'])
    temp = temp + 24
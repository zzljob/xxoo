#!/usr/bin/python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import requests
import time
import json

import leancloud
from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError

import xxxiao


APP_ID = "APP_ID"
APP_KEY = "APP_KEY"
leancloud.init(APP_ID, APP_KEY)

def saveImage(url) :
	ImageObject = Object.extend('XXXiaoImage')
	img = ImageObject();
	img.set("url", url);
	try:
		img.save()
	except LeanCloudError, e:
		print e
	file_path = 'xxxiao/[%d-%d]%s%s' % (page_num, index, title, img_url[img_url.rindex('.'):])
	print '[%d] %s => %s' % (index, title, file_path)
	with open(file_path, 'wb') as img_file:
		img_file.write(requests.get(img_url, stream=True).content)
	

def saveToLocal(item, dir = 'xxxiao'):
	img_url = item['cover']
	title = item['title']
	if not os.path.exists(dir):
		os.makedirs(dir)
	file_path = '%s/%s%s' % (dir, title, img_url[img_url.rindex('.'):])
	print '[%d] %s => %s' % (index, title, file_path)
	with open(file_path, 'wb') as img_file:
		img_file.write(requests.get(img_url, stream=True).content)
		
		
####开端

page = xxxiao.fetchImageSeriesByPageNum(1)
page_content = []
for index, each in enumerate(page['list']):
	node = page['list'][index];
	date = time.strftime('%Y-%m-%d',time.localtime(time.time()));
	href = "#";
	page_content.append({"img":node['cover'],"title":node["title"],"href":href,"author":"auto","date":date});

with open("./images.json", 'wb') as json_file:
	json_file.write(json.dumps(page_content))
	


	

	
	
	
	
	
	
	

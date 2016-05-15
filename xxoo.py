#!/usr/bin/python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import requests

import leancloud
from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError

import xxxiao


APP_ID = "5o0TpmUu18wHbc43boVcYccx-gzGzoHsz"
APP_KEY = "M0hg5yOIa5AhRTS8TRXw5NMH"
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
for index, each in enumerate(page['list']):
	saveToLocal(each, 'xxxiao/%d' % (page['page']))

while(page != None and page['previous'] != None and page['page'] > 0 and page['page'] < 50):
	page = xxxiao.fetchImageSeriesByUrl(page['previous'])
	if page == None:
		break
		
	for index, each in enumerate(page['list']):
		saveToLocal(each, 'xxxiao/%d' % (page['page']))
	

	
	
	
	
	
	
	
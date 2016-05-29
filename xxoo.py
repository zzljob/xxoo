#!/usr/bin/python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import requests
import time
import json
import sqlite3

import xxxiao
import dbstorge

####开端

# page = xxxiao.fetchImageSeriesByPageNum(1)
# page_content = []
# for index, each in enumerate(page['list']):
# 	node = page['list'][index];
# 	date = time.strftime('%Y-%m-%d',time.localtime(time.time()));
# 	href = "#";
# 	page_content.append({"img":node['cover'],"title":node["title"],"href":href,"author":"auto","date":date});
#
# with open("./images.json", 'wb') as json_file:
# 	json_file.write(json.dumps(page_content))

def saveSeriesToDB(conn, page):
	exists = 0
	insert = 0
	for index, each in enumerate(page['list']):
		node = page['list'][index]
		cover = node['cover']
		link = node['link']
		title = node['title']
		# print node
		series = dbstorge.getSeriesByLink(conn, link)
		if series and len(series) > 0 :
			exists += 1
			# print 'exists', link
		else :
			insert += 1
			# print 'insert', link
			dbstorge.saveSeries(conn, title, link, cover)
	return {'exists':exists, 'insert':insert}


dbfile = "xxoo.db"
conn = sqlite3.connect(dbfile)
# print "Opened database successfully";

page_num = 1
while page_num <= 10000:
	page = xxxiao.fetchImageSeriesByPageNum(page_num)
	if page == None or page['list'] == None or len(page['list']) <= 0:
		print 'continue, page =', page
		continue
	print 'page =', page['page'], '=>', saveSeriesToDB(conn, page)
	if page['previous'] == None:
		print 'break, page[previous] =', page['previous']
		break
	page_num += 1

conn.close()

# print dbstorge.getSeriesByLink(conn, '12')
# print dbstorge.saveSeries(conn, "title", "link", "cover")
# print dbstorge.saveSeriesOrgicover(conn, 'orgicover', link)

print 'finish'

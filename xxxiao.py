#!/usr/bin/python
#coding=utf-8

import requests
from bs4 import BeautifulSoup

def fetchImageSeriesByPageNum(page_num) :
	return fetchImageSeriesByUrl('http://m.xxxiao.com/page/%d' % (page_num))

def getPageNumByUrl(url):
	if url != None and url.startswith('http://m.xxxiao.com/page/') and int(url[url.rindex('/')+1:]) > 0:
		return int(url[url.rindex('/')+1:])
	else:
		return -1

def fetchImageSeriesByUrl(page_url) :
	res = requests.get(page_url)
	html = BeautifulSoup(res.text, "html.parser")

	page_content = []
	for index, each in enumerate(html.select('#blog-grid article')):
		titleNode = each.select('h2.entry-title a')[0]
		title = titleNode.text
		link = titleNode.get('href')
		img_url = each.select('img')[0].get('src')
		tag = each.select('span.entry-cats a')[0].text

		page_content.append({'title':title, 'link':link, 'cover':img_url, 'tag':tag})

	nav_node = html.select('nav.paging-navigation div.nav-links')[0]

	page_previous = None
	previous_a_node = nav_node.select('div.nav-previous a')
	if len(previous_a_node) > 0 :
		page_previous = previous_a_node[0].get('href')

	page_next = None
	next_a_node = nav_node.select('div.nav-next a')
	if len(next_a_node) > 0 :
		page_next = next_a_node[0].get('href')

	return {'list':page_content, 'previous': page_previous, 'next': page_next, 'page': getPageNumByUrl(page_url)}

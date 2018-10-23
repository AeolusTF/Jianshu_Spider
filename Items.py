# -*- coding:utf-8 -*-

# Define here the modeis for your scraped items
# 
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JianshuItem(scrapy.Item):
	#define the fields for you item here like:
	#name = scrapy.Field()
	title = scrapy.Field()  #可以理解成字典
	author = scrapy.Field()
	url = scrapy.Field()
	readNum = scrapy.Field()
	commentNum = scrapy.Field()
	likeNum = scrapy.Field()

	
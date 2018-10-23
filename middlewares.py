# -*- coding:utf-8 -*-

# Define here the models for your spider middleware
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from user_agent import agents


class UserAgentMiddleware(object):
	#Not all methods need to be defined. If a method is not defined,
	#scrapy acts as if the spider middleware does not modify the
	#oassed objects.
	'''随机获取浏览器的头部信息'''

	def process_request(self,request,spider):
		agent = random.choice(agents)
		request.headers["User_Agent"] = agent



class ProxyModdleware()
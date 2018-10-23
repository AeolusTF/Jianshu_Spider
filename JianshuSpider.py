#-*- coding:utf8 -*-


import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from Jianshu.item import JianshuItem


class Jianshu(scrapy.Spider):
	name = 'Jianshu'

	url = 'http://www.Jianshu.com' #拼接封面图

	def start_requests(self): #生成url
		for i in range(1,5):
			url = 'http://www.Jianshu.com/monthly?&page={}'.format(i) 
			yield Request(url,callback=self.parse)


	def parse(self,response):
		items = JianshuItem()  #实例存储数据的容器
		selector = Selector(response)
		articles = selector.xpath('//ul[@class="note-list"]/li') #获取每一篇文章的数据 编译

		for article in articles: #便历
			title = article.xpath('div/a/text()').extract() #把对象变成具体的数据
			url = article.xpath('div/a/@href').extract()
			author = article.xpath('div/div[1]/div/a/text()').extract()


			#没有封面图  做异常处理
			try:
				image = article.xpath('a/img/@src').extract()
				with open('D:/image/%s-%s.jpg'%(author[0],title[0]),'wb') as f:
					f.write(requests.get('http://'+image[0].content)) #图片的二进制数据
			except Exception as e:
				print '--no--image'

			readNum = article.xpath('div[@class="content"]/div[@class="meta"]/a[1]/text()') #1代表的第一个/a标签

			commentNum = article.xpath('div[@class="content"]/div[@class="meta"]/a[2]/text()')

			likeNum = article.xpath('div[@class="content"]/div[@class="meta"]/span[1]/text()')

			items['title'] = title[0]
			items['url'] = url[0]
			items['author'] = author[0]
			items['readNum'] = readNum[0]
			items['commentNum'] =commentNum[0]
			items['likeNum'] = likeNum[0]

			yield items
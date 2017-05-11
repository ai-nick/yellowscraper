


import scrapy
import json
from archery.items import archeryItem

class archerySpider(scrapy.Spider):
    name = "arch"
    def start_requests(self):
		stateFile = open('states.json').read()
		states = json.loads(stateFile)
		for state in states:
			re = scrapy.Request("https://www.yellowpages.com/search?search_terms=archery&geo_location_terms="+state['stateAbv'],
			callback=self.parse)
			re.meta['state'] = state
			yield re

    def parse(self, response):
		base = 'https://www.yellowpages.com'
		state = response.meta['state']
		urls = response.xpath('//h2[@class="n"]/a/@href').extract()
		for u in urls:
			newU = base+u
			request = scrapy.Request(newU, callback=self.get_email)
			request.meta['state'] = state
			yield request
			
		next_page = response.xpath('//li/a[contains(text(), "next")]/@href')
		if next_page:
			url = base+next_page
			nextpage = scrapy.Request(url, self.parse)
			nextpage.meta['state'] = state
			yield nextpage

		
    def get_email(self, response):
		state = response.meta['state'] 
		outfitter = archeryItem()
		outfitter['outfitter'] = response.xpath('//div[@class="sales-info"]/h1/text()').extract_first()
		outfitter['email'] = response.xpath('//a[starts-with(@href, "mailto")]/@href').extract_first()
		outfitter['state'] = state
		yield outfitter
		
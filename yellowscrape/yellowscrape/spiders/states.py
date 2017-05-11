import scrapy
from archery.items import stateItem

class archerySpider(scrapy.Spider):
    name = "states"
    start_urls = [
        'http://www.softschools.com/social_studies/state_abbreviations/',
    ]

    def parse(self, response):
		states = response.xpath('//tr[@align="left"]/td[2]/text()').extract()
		for row in states:
			state = stateItem()
			state['stateAbv'] = row
			yield state

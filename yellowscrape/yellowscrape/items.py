# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class archeryItem(scrapy.Item):
		state = scrapy.Field()
		outfitter = scrapy.Field()
		email = scrapy.Field()
		phone = scrapy.Field()
		website = scrapy.Field()
		webBool = bool
		
class stateItem(scrapy.Item):
		stateAbv = scrapy.Field()


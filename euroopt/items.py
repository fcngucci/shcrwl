# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EurooptItem(scrapy.Item):
    
    global_name = scrapy.Field()
    global_link = scrapy.Field()

    categ_name = scrapy.Field()
    categ_link = scrapy.Field()

    prods_name = scrapy.Field()
    prods_link = scrapy.Field()

class ProdItem(scrapy.Item):

	item_name = scrapy.Field()
	item_link = scrapy.Field()
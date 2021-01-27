import mysql.connector
import scrapy
import time

from ..items import ProdItem

class ProdsPage(scrapy.Spider):

	name = "prods_page"
	allowed_domains = ["e-dostavka.by"]

	def __init__(self, name=None):
		super(ProdsPage, self).__init__()
		self.conn = mysql.connector.connect(db='euroopt', user='root', password='856940TIpo$')
		self.cur = self.conn.cursor()

	def start_requests(self):

		def init_connection():
			query = (
				'SELECT prods_link '
				'FROM main'
				)
			self.cur.execute(query)

			for link in self.cur:
				yield link[0]

		for link in init_connection():
			yield scrapy.Request(link, self.parse)

	def parse(self, repsonse):
		
		page_sel = '/html/head/meta[3]/@name'
		desreq = repsonse.xpath(page_sel).get()
		p_s = '/html/head/meta[3]/@content'
		conreq = repsonse.xpath(p_s).get()

		if desreq == "description" and ("Следующая страница" not in conreq):
			sel = '//div[@class="form_wrapper"]/form/div[@class="title"]/a'
			product = ProdItem()
			for info in repsonse.xpath(sel):
				product['item_name'] = info.xpath('text()').get()
				product['item_link'] = info.xpath('@href').get()
				yield product
			if "lazy_steep" in repsonse.url:
				splitor = 'lazy_steep='
				url_list = repsonse.url.split(splitor)
				page_n = str(int(url_list.pop())+1)
				url_list.append(page_n)
				link = splitor.join(url_list)
				yield scrapy.Request(link, self.parse)
			else:
				link = repsonse.url+"?lazy_steep=2"
				yield scrapy.Request(link, self.parse)
		time.sleep(1)
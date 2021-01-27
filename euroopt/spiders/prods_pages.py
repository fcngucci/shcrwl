import mysql.connector
import scrapy

class ProdsPage(scrapy.Spider):

	name = "prods_page"
	allowed_domains = ["e-dostavka.by"]

	def start_requests(self):

		def init_connection():

			conn = mysql.connector.connect(db='euroopt', user='root', password='856940TIpo$')
			cur = conn.cursor()
			query = (
				'SELECT prods_link '
				'FROM main'
				)
			cur.execute(query)

			for link in cur:
				yield link[0]

		n = 1
		for link in init_connection():
			yield scrapy.Request(link, self.parse)
			n+=1
			if n == 100:
				break

	def parse(self, repsonse):

		sel = '//div[@class="form_wrapper"]/form/div[@class="title"]/a'
		f = open('test.txt', 'a')
		f.write(str(repsonse.request.headers['User-Agent'])+"\n")
		for info in repsonse.xpath(sel):
			f.write(info.xpath('@href').get()+'\t'+info.xpath('text()').get()+'\n')
		f.close()
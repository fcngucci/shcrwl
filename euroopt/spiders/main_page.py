from ..items import EurooptItem
	
import scrapy

class MainEdostavka(scrapy.Spider):

	name = "e_main"
	allowed_domains = ["e-dostavka.by"]
	start_urls = ["https://e-dostavka.by"]

	def parse(self, response):
		
		info_sel = ['a/text()', 'a/@href']
		main_sel = ['ul/li', 'div/ul/li', '//ul[@class="catalog_menu catalog_menu_visible"]/li']	

		euroopt = EurooptItem()

		for main in response.xpath(main_sel[2]):

			euroopt['global_name'] = main.xpath(info_sel[0]).get()
			euroopt['global_link'] = main.xpath(info_sel[1]).get()

			for main in main.xpath(main_sel[1]):
				
				euroopt['categ_name'] = main.xpath(info_sel[0]).get()
				euroopt['categ_link'] = main.xpath(info_sel[1]).get()

				for main in main.xpath(main_sel[0]):
					
					euroopt['prods_name'] = main.xpath(info_sel[0]).get()
					euroopt['prods_link'] = main.xpath(info_sel[1]).get()

					yield euroopt
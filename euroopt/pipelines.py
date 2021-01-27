# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector


class EurooptPipeline:
    def process_item(self, item, spider):
        return item



class ItemPipeline(object):

	def process_item(self, item, spider):
		self.conn = mysql.connector.connect(db='euroopt', user='root', password='856940TIpo$', host='localhost')
		self.cursor = self.conn.cursor()

		insert_sql = "INSERT INTO main(categ_link, categ_name, global_link, global_name, prods_link, prods_name) VALUES (%s,%s,%s,%s,%s,%s)"
		
		
		self.cursor.execute(insert_sql,
			(
				item.get('categ_link'), item.get('categ_name'), item.get('global_link'),
				item.get('global_name'), item.get('prods_link'), item.get('prods_name')
				)
			)
		self.conn.commit()
		return item
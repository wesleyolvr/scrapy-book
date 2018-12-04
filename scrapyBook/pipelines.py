# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class ScrapyBookPipeline(object):
    def process_item(self, item, spider):
        if float(str(item['preco'].replace('£',''))) > 20:
            return item
        else:
            Dropitem('valor menos que £20')

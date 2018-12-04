# -*- coding: utf-8 -*-
import scrapy

class BooksSpider(scrapy.Spider):
    name = "diariophb"
    start_urls = [
        ' http://dom.parnaiba.pi.gov.br/home?d=1',
    ]

    def parse(self, response):
        pass
        
# -*- coding: utf-8 -*-
import scrapy
from scrapyBook.items import BooksItem
class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'http://books.toscrape.com/',
    ]

    def parse(self, response):
        for book_url in response.xpath('//article[@class="product_pod"]//a/@href').extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book_page)
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_book_page(self, response):
        item = BooksItem()
        produto = response.xpath('//article[@class="product_page"]')
        item["titulo"] = produto.xpath('//h1/text()').extract_first()
        item['categoria'] = response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').extract_first()
        item['descricao'] = produto.xpath('./p/text()').extract_first()
        item['preco'] = produto.xpath('//p[@class="price_color"]/text()').extract_first()
        yield item




# -*- coding: utf-8 -*-
import scrapy


class WySpider(scrapy.Spider):
    name = "wy"
    allowed_domains = ["163.com"]
    start_urls = (
        'http://www.163.com/',
    )

    def parse(self, response):
        pass

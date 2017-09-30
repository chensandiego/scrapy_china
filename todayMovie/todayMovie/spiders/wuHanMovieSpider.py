# -*- coding: utf-8 -*-
import scrapy
from todayMovie.items import TodaymovieItem


class WuhanmoviespiderSpider(scrapy.Spider):
    name = 'wuHanMovieSpider'
    allowed_domains = ['jycinema.com']
    start_urls = ('http://www.jycinema.com/browsing/Cinema/Details/1029',)

    def parse(self, response):
        subSelector=response.xpath('//div[@class="film-header"]')
        items=[]
        for sub in subSelector:
            item = TodaymovieItem()
            item['movieName'] = sub.xpath('./a/h3/text()').extract()
            item.append(item)
        return items

# -*- coding: utf-8 -*-
import scrapy
import requests
from indeed.items import IndeedItem

class IndeedSpider(scrapy.Spider):

    name = 'indeed'
    allowed_domains = ['indeed.com.br']
    start_urls = ['https://www.indeed.com.br/jobs?q=desenvolvedor&l=São+Paulo']

    # def start_requests(self):

    #     start_url = ['https://www.indeed.com.br/jobs?q=desenvolvedor&l=São+Paulo']

    #     # for i in range(10, 60, 10):
    #     #    yield scrapy.Request(url = url.format(str(i))
    #     yield scrapy.Request(url, callback=self.scrape)
    
    def parse(self, response):        
        item = IndeedItem()

        company = response.xpath("""//*[@class="company"]//text()""").extract()
        company = [i.strip() for i in company if i.strip()]
        item['company'] = company
        
        yield item
        


        
        
    
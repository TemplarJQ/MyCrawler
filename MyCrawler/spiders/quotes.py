# -*- coding: utf-8 -*-
import scrapy
from MyCrawler.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # print(response.text)
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            # extract返回的是列表，first是第一个元素
            tags = quote.css('.tags .tag::text').extract()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

        next = response.css('.pager .next a::attr(href)').extract_first()
        # 获取绝对地址
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse) # dont_filter=True该参数会导致网页不停爬取


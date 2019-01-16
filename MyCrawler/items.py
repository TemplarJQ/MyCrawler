# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class MycrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuoteItem(scrapy.Item):
    # code for quotes.toscrope.com
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
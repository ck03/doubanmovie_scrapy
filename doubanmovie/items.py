# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    cover = scrapy.Field()
    id = scrapy.Field()
    is_new = scrapy.Field()
    playable = scrapy.Field()
    rate = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()



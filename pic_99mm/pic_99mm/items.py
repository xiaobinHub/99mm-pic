# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Pic99MmItem(scrapy.Item):
    title = scrapy.Field()
    pic_url = scrapy.Field()
    pic_num = scrapy.Field()
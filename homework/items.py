# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

import json







class PTTArticleItem(scrapy.Item):
    url = scrapy.Field()
    article_id = scrapy.Field()
    article_author = scrapy.Field()
    article_title = scrapy.Field()
    article_date = scrapy.Field()
    article_content = scrapy.Field()
    ip = scrapy.Field()
    message_count = scrapy.Field()
    messages = scrapy.Field()



class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class ScrapyXywyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuestionItem(Item):
    """问题"""
    title = Field() # 标题
    description = Field() # 描述
    answer = Field() # 回复
    tag = Field() # 问题标签
    category = Field() # 分类
    source = Field() # 来源


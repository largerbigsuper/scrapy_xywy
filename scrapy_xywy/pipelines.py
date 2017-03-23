# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exceptions import DropItem


class ScrapyXywyPipeline(object):
    def process_item(self, item, spider):
        return item

class QuestionPipeline(object):
    """问题保存"""

    def __init__(self):
        self.file = open('questions.jl', 'wb')

    def process_item(self, item, spider):
        if not item['title']:
            raise DropItem("无效的drug")
        else:
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            line = unicode.encode(line, 'utf-8')
            self.file.write(line)
            return item


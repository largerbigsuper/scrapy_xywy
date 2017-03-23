#_*_coding:utf-8_*_

# http://club.xywy.com/keshi/1.html
from string import Template

import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.exceptions import IgnoreRequest

# 问题按日期分类页
# http://club.xywy.com/keshi/1.html
# 问题列表页
# http://club.xywy.com/keshi/2017-03-21/1.html
# 问题详情页
# http://club.xywy.com/static/20170322/127614906.htm
from scrapy_xywy.items import QuestionItem


class QuestionSpider(scrapy.Spider):
    """一问一答"""

    name = 'questions'

    base_url = Template("http://club.xywy.com/keshi/$data/$page")
    def start_requests(self):
        url = self.base_url.substitute({"data":"2017-03-21", "page":"1.html"})
        url2 = self.base_url.substitute({"data":"2017-03-22", "page":"1.html"})
        url3 = self.base_url.substitute({"data":"2017-03-20", "page":"1.html"})
        request = scrapy.Request(url=url, callback=self.parse)
        request2 = scrapy.Request(url=url2, callback=self.parse)
        request3 = scrapy.Request(url=url3, callback=self.parse)

        yield request
        yield request2
        # yield request3


    def parse(self, response):
        """处理问题列表"""
        html = response.text # 不是用response.body
        soup = BeautifulSoup(html, "lxml")
        # 判断是否有下一页
        nextpage = soup.find_all('a', text='[下一页]')
        print  nextpage
        if nextpage:
            page = nextpage[0].get('href')
            data = response.url.split('/')[-2]
            url = self.base_url.substitute({"data":data, "page":page})
            print "==============" + url + "================="
            yield scrapy.Request(url=url, callback=self.parse)
        else:
            pass
        # 提前问题url
        divList = soup.find_all('div', attrs={"class":"club_dic"})
        for i in xrange(len(divList)):
            url = divList[i].find('em').a.get('href')
            yield scrapy.Request(url=url, callback=self.qusetion_parse)

        """
        <p class="pt10 pb10 lh180 znblue normal-a">
        <a href="http://club.xywy.com/" target="_blank">有问必答</a> &gt;
        <a href="http://club.xywy.com/kswd_list.htm" target="_blank">全部问题</a> &gt;
        <a href="http://club.xywy.com/big_287.htm" target="_blank">妇产科</a> &gt;
        <a href="http://club.xywy.com/small_556.htm" target="_blank">月经不调</a> &gt;
        月经推迟两个星期验尿没有怀孕请问什么原因	</p>
        """

    def qusetion_parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        """
        <p class="pt10 pb10 lh180 znblue normal-a">
        <a href="http://club.xywy.com/" target="_blank">有问必答</a> &gt;
        <a href="http://club.xywy.com/kswd_list.htm" target="_blank">全部问题</a> &gt;
        <a href="http://club.xywy.com/big_287.htm" target="_blank">妇产科</a> &gt;
        <a href="http://club.xywy.com/small_556.htm" target="_blank">月经不调</a> &gt;
        月经推迟两个星期验尿没有怀孕请问什么原因	</p>
        """
        # 分类
        tab = soup.find('p', attrs={"class":"pt10 pb10 lh180 znblue normal-a"})
        if not tab:
            yield scrapy.Request(url=response.url, callback=self.qusetion_parse)
        category = tab.find_all('a')[2].string
        tag = tab.find_all('a')[3].string
        title = soup.find('p', attrs={"class":"fl dib fb"}).get('title')
        # description = soup.find('div', attrs={"id":"qdetailc"}).string
        # 问题内容可能有表格形式
        desc_strings = soup.find('div', attrs={"id":"qdetailc"}).stripped_strings
        desc_list = []
        for string in desc_strings:
            desc_list.append(string)
        if len(desc_list) > 1:
            description = desc_list[1]
        else:
            description = desc_list[0]
        print description

        # answer = soup.find_all('div', attrs={"class":"pt15 f14 graydeep  pl20 pr20"})
        answer_div = response.xpath("//div[@class= 'pt15 f14 graydeep  pl20 pr20']")
        if not answer_div:
            return
        print "---------------------------------"
        print answer_div
        text_list = answer_div[0].xpath('text()').extract()
        answer = ''
        for i in xrange(len(text_list)):
            answer  = answer + text_list[i]
        source = response.url

        item = QuestionItem()
        item['title'] = title
        item['description'] = description
        item['answer'] = answer
        item['tag'] = tag
        item['category'] = category
        item['source'] = source

        yield item






class TestSpider(scrapy.Spider):
    name = 'testpider'

    start_urls = [
        # 'http://club.xywy.com/static/20140801/49588671.htm',
        # 'http://club.xywy.com/static/20170322/127617181.htm',
        # 'http://club.xywy.com/static/20170323/127621121.htm'
        'http://club.xywy.com/static/20170321/127601416.htm',
        'http://club.xywy.com/static/20170321/127601390.htm',
        'http://club.xywy.com/static/20170321/127601391.htm',
    ]

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        """
        <p class="pt10 pb10 lh180 znblue normal-a">
        <a href="http://club.xywy.com/" target="_blank">有问必答</a> &gt;
        <a href="http://club.xywy.com/kswd_list.htm" target="_blank">全部问题</a> &gt;
        <a href="http://club.xywy.com/big_287.htm" target="_blank">妇产科</a> &gt;
        <a href="http://club.xywy.com/small_556.htm" target="_blank">月经不调</a> &gt;
        月经推迟两个星期验尿没有怀孕请问什么原因	</p>
        """
        # 分类
        tab = soup.find('p', attrs={"class":"pt10 pb10 lh180 znblue normal-a"})
        if not tab:
            return
        category = tab.find_all('a')[2].string
        tag = tab.find_all('a')[3].string
        title = soup.find('p', attrs={"class":"fl dib fb"}).get('title')
        # description = soup.find('div', attrs={"id":"qdetailc"}).string
        # 问题内容可能有表格形式
        desc_strings = soup.find('div', attrs={"id":"qdetailc"}).stripped_strings
        desc_list = []
        for string in desc_strings:
            desc_list.append(string)
        if len(desc_list) > 1:
            description = desc_list[1]
        else:
            description = desc_list[0]
        print description

        # answer = soup.find_all('div', attrs={"class":"pt15 f14 graydeep  pl20 pr20"})
        answer_div = response.xpath("//div[@class= 'pt15 f14 graydeep  pl20 pr20']")
        if not answer_div:
            return
        print "---------------------------------"
        print answer_div
        text_list = answer_div[0].xpath('text()').extract()
        answer = ''
        for i in xrange(len(text_list)):
            answer  = answer + text_list[i]
        source = response.url

        item = QuestionItem()
        item['title'] = title
        item['description'] = description
        item['answer'] = answer
        item['tag'] = tag
        item['category'] = category
        item['source'] = source

        yield item



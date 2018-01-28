# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from pic_99mm.items import Pic99MmItem

class MmSpider(scrapy.Spider):
    name = 'mm'
    #allowed_domains = ['99mm.me']
    start_urls = ['http://www.99mm.me/meitui/','http://www.99mm.me/xinggan/','http://www.99mm.me/qingchun/','http://www.99mm.me/hot/']

    def parse(self, response):
        
        list = response.xpath('//ul[@id="piclist"]/li')

        for l in list:
            lin = ''.join(l.xpath('./dl/dt/a/img/@src').extract())   
            title = ''.join(l.xpath('./dl/dt/a/img/@alt').extract())  
            b_link = lin.replace('/small','').replace('.jpg','').replace('*/','')
            album_id = re.findall(r'(\w*[0-9]+)\w*', b_link)[2]
            header = {
                "Accept":"*/*",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
                "Host":"www.99mm.me",
                "Proxy-Connection":"keep-alive",
                "Referer":"http://www.99mm.me/meitui/{}.html",
                "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
                .format({},album_id)
            }
            ge_pic_id_url = 'http://www.99mm.me/url.php?act=view&id=' + str(album_id)
            pic_ids= requests.get(ge_pic_id_url,headers = header).text.split(",")
            pic_num = 1
            for pic_id in pic_ids:
                item = Pic99MmItem()
                pic_url = b_link + '/' + str(pic_num) + '-' + str(pic_id) + '.jpg'
                item['title'] = title
                item['pic_url'] = pic_url
                item['pic_num'] = pic_num
                yield item
                pic_num = pic_num + 1

        next_page = ''.join(response.xpath('//div[@class="page"]/a[@class="next"]/@href').extract())
        if next_page:
            
            if 'hot' in response.url:
                t = 'http://www.99mm.me/hot/'
            if 'meitui' in response.url:
                t = 'http://www.99mm.me/meitui/'
            if 'xinggan' in response.url:
                t = 'http://www.99mm.me/xinggan/'
            if 'qingchun' in response.url:
                t = 'http://www.99mm.me/qingchun/' 

            next_page_url = t + next_page 
            yield scrapy.Request(next_page_url,callback = self.parse)







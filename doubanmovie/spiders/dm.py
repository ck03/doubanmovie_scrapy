# -*- coding: utf-8 -*-
import scrapy
import json
from doubanmovie.items import DoubanmovieItem
import re


class DmSpider(scrapy.Spider):
    name = 'dm'
    allowed_domains = ['movie.douban.com']
    # start_urls = ["https://movie.douban.com/top250"]
    # 遇到無法進到parse 裡.原來 DEBUG: Forbidden by robots.txt
    # 把settings裡的ROBOTSTXT_OBEY = False 改為False就可以了
    pg = 0
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0']
    next_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'

    print("爬蟲開始..........")

    def parse(self, response):
        dm_dict = json.loads(response.body_as_unicode())
        # print(dm_dict)
        dm_list = dm_dict["subjects"]
        # print(len(dm_list))
        if len(dm_list) > 0:
            for dm in dm_list:
                item = DoubanmovieItem()
                item["cover"] = dm["cover"]
                item["id"] = dm["id"]
                item["is_new"] = dm["is_new"]
                item["playable"] = dm["playable"]
                item["rate"] = dm["rate"]
                item["title"] = dm["title"]
                item["url"] = dm["url"]
                yield item
            # print("end")
            # 下一頁
            self.pg += 1
            next_url = self.next_url.format(self.pg * 20)
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
        else:
            # 最後沒有資料時回傳一個空item{}回pipelines,告訴它可以保存資料到json,csv,or db
            # 或是可以在pipelines.py裡的close_spider()寫作
            item = DoubanmovieItem()
            yield item
            print("爬蟲結束.........,pg=%d" % (int(self.pg)*19))

        # print(next_url)


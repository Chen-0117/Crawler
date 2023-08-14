import scrapy
from general.items import GeneralItem

class DianwangSpider(scrapy.Spider):
    name = "dianwang"
    allowed_domains = ["www.chinapower.com.cn"]
    start_urls = ["http://www.chinapower.com.cn/zx/hyfx/20230731/211282.html"]

    def parse(self, response):
        rl = []
        head = response.css('div > h1').xpath("//h1/text()").extract()[0]
        item = GeneralItem()
        item['head'] = head
        rl.append(item)
        title = response.css('p > strong').xpath("//strong/text()").extract()
        for each in title:
            item = GeneralItem()
            item['title'] = each
            rl.append(item)
        content_list = response.css('div > p')
        for i in range(len(content_list)):
            item = GeneralItem()
            each = content_list[i].xpath("//p[{}]/text()".format(i+1)).extract()
            if each:
                item['content'] = each
            rl.append(item)
        # print(content_list)
        # print(len(content_list))
        # for item in content_list:
        #     g = GeneralItem()
        #     if item
        return rl

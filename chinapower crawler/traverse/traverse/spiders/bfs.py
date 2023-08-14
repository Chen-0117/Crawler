import scrapy
from traverse.items import TraverseItem

class BfsSpider(scrapy.Spider):
    name = "bfs"
    allowed_domains = ["www.chinapower.com.cn"]
    start_urls = ["http://www.chinapower.com.cn/zx/"]

    def parse(self, response):
        l = response.css("a::attr(href)").extract()
        nl = []
        for each in l:
            if each.find('http') == -1:
                new = "http://www.chinapower.com.cn" + each
                nl.append(new)
            else:
                nl.append(each)

        al = []
        for link in nl:
            if link not in al:
                yield scrapy.Request(link, callback=self.parse)
                al.append(link)

        rl = []
        head = response.css('div > h1').xpath("//h1/text()").extract()[0]
        item = TraverseItem()
        item['title'] = head
        rl.append(item)
        title = response.css('p > strong').xpath("//strong/text()").extract()
        for each in title:
            item = TraverseItem()
            item['subtitle'] = each
            rl.append(item)
        content_list = response.css('div > p')
        for i in range(len(content_list)):
            item = TraverseItem()
            each = content_list[i].xpath("//p[{}]/text()".format(i+1)).extract()
            if each:
                item['paragraph'] = each
            rl.append(item)
        
        return rl



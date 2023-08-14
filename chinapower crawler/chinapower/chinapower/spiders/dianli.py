import scrapy
from chinapower.items import ChinapowerItem


class DianliSpider(scrapy.Spider):
    name = "dianli"
    allowed_domains = ["www.chinapower.com.cn"]
    start_urls = ["http://www.chinapower.com.cn/zx/zxbg/20230804/212043.html"]

    def parse(self, response):
        # a = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]").extract()[0]
        # b = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/p[4]/text()").extract()[0].replace(u'\u3000',u'').replace('\n', '').replace('\r', '').replace(' ','')
        # print(b)
        # c = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/p[45]")
        # p1 = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/p[1]")
        # print(not p1)
        # p2 = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/p[1]").extract()[0]
        # print(not p2)
        # print(c)
        # # e = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/p[4]/text").extract()
        # d = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/p[3]").extract()[0].replace(u'\u3000',u'').replace('\n', '').replace('\r', '').replace(' ','')
        # print(d)
        i = 1
        items = []
        while True:
            item = ChinapowerItem()
            # p1 = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/p[13]").extract()
            # print(p1)
            # p2 = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/p[12]/text()").extract()[0].replace(u'\u3000',u'').replace('\n', '').replace('\r', '').replace(' ','')
            # print(p2)
            p = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/p[{}]".format(i)).extract()
            if not p:
                break
            text = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/p[{}]/text()".format(i)).extract()
            if not text:
                pass
            item['material'] = text
            i += 1
            items.append(item)
        # context = response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/p[4]/text()")
        # content = context.extract()
        # print(content)
        # item = ChinapowerItem()
        # item.material = content[0]
        # pass
        # filename = 'data.txt'
        # with open(filename, 'w') as re:
        #     re.write(response.body)
        return items

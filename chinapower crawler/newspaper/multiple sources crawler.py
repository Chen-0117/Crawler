import newspaper
import pandas as pd
from newspaper import Config



user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 30
url = 'http://www.chinapower.com.cn/sj/'
dianli1 = newspaper.build(url, language = 'zh',memoize_articles=False,config=config)
print(dianli1)
# for category in dianli.category_urls():
#     print(category)

title = []
content = []
author = []
keywords = []
summary = []
print(len(dianli1.articles))
news = dianli1.articles
# news.download()
# news.parse()
# print(news.title)
# print(news.text)
for i in range(len(news[:30])):
    each = news[i]
    try:
        each.download()
        each.parse()
        title.append(each.title)
        content.append(each.text)
        author.append(each.authors)
        keywords.append(each.keywords)
        summary.append(each.summary)
    except:
        title.append('NULL')
        content.append('NULL')
        author.append('NULL')
        keywords.append('NULL')
        summary.append('NULL')
        continue

data = pd.DataFrame({'title':title, 'author': author, 'keywords': keywords, 'summary': summary, 'content':content})
# data = pd.DataFrame({'title':title, 'content':content})
print(data)
data.to_json("data.json", force_ascii=False)
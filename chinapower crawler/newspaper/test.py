from newspaper import Article
from newspaper import Config
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 20
url = "https://sgnec.sgcc.com.cn/policydetailNew/?newsId=2308080404300105403"
news = Article(url, language='zh',config=config)
news.download()
news.parse()
print('题目', news.title)
print('正文', news.text.strip())
print('作者', news.authors)
print('关键词', news.keywords)
print('概况', news.summary)
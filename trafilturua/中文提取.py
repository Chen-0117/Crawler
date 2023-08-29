import re

with open("C:/Users/dell/Desktop/chinapower crawler/trafiltura/中国华能.txt", 'r', encoding='utf-8') as f:
    s = f.readline()
    print(len(s))
 
#提取中文字符
# https://blog.csdn.net/COCO56/article/details/87618925
string_code = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u3002\uff1f\uff01\uff0c\u3001\uff1b\uff1a\u300a-\u300f\u2018\u2019\u201c\u201d\uff08\uff09\u3014\u3015\u3009-\u3011\u2014\u2016\u2013\uff0e])","",s)
print(string_code)
with open("C:/Users/dell/Desktop/chinapower crawler/trafiltura/中国华能清洗.txt", 'w', encoding='utf-8') as fw:
    fw.write(string_code)
              
    

import json

path = "C:/Users/dell/Desktop/chinapower crawler/extracted_content中国华能大.json"
 
# file = open(path, 'r',encoding='utf-8')
# file1 = open("C:/Users/dell/Desktop/chinapower crawler/trafiltura/结果.txt", 'w')

data = []
# with open(path, 'rb') as f:
#     for line in f:
#         if line:
#             data.append(json.loads(line))
#     print(data)
#     for item in data:
#         with open("C:/Users/dell/Desktop/chinapower crawler/trafiltura/结果.txt", 'w', encoding="utf-8") as f1:
#             f1.write(item['content'])


try:
    with open(path, 'rb') as json_file:
        data = json.load(json_file)
except json.JSONDecodeError as e:
    print("JSON Decode Error:", e)

# with open(path, 'rb') as json_file:
#         data = json.load(json_file)
# print(data['content']['0'])
s = ''
# for i in range(len(data['content'])):
#     # print(item)
#     # print(data['content'][str(i)])
#     ss = data['content'][str(i)].strip().replace('\n','')
#     s += ss
for item in data:
    s += item['content'].strip().replace('\n','')
with open("C:/Users/dell/Desktop/chinapower crawler/trafiltura/中国华能.txt", 'w', encoding="utf-8") as f:
    f.write(s)
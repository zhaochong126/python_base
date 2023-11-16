import requests
import re
import parsel
import time
url = input('输入你要获取的小说地址：')#获取章节href
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60',
    'Referer':'https://fanqienovel.com/'
}
resp = requests.get(url, headers)
# print(resp.text)
noval_name = re.findall('<h1>(.*?)</h1>', resp.text)[0]
noval_info = re.findall('<dd><a href ="(.*?)">(.*?)</a></dd>', resp.text)
# print(noval_name)
# print(noval_info)
for noval_url,noval_title in noval_info:
    noval_url1='https://www.bige3.cc/'+noval_url
    # print(noval_url1)
    # print(noval_title)



# url = 'https://www.bige3.cc/book/77547/1.html'


    resp = requests.get(url=noval_url1,headers=headers)
    html_data = resp.text#拿到网页数据
    # print(html_data)
    selector = parsel.Selector(html_data)#解析数据
    # noval_title = selector.css('.content h1::text').get()#筛选小说名
    noval_content = selector.css('#chaptercontent::text').getall()#筛选小说内容
    content='\n'.join(noval_content)
    # print(noval_title)
    # # print(noval_content)
    # print(content)
    with open(noval_name+'.txt', mode='a', encoding='utf-8') as f:#保存数据
        f.write(noval_title)
        f.write('\n')
        f.write(content)
        f.write('\n')
        time.sleep(0.0000000001)
    print('正在保存',noval_title)
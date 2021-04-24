import time

import requests
from bs4 import BeautifulSoup
import pandas as pd
start = time.time()
a = input("你要搜索什么:")
dts = []
for i in range(1, 51):
    print(i)
    print(a)
    url = 'https://search.bilibili.com/all?keyword=' + a + '&page=%d' % (i)
    print(url)
    html = requests.get(
        url, headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'},
        timeout=30)  # 获取网页
    time.sleep(2)
    soup = BeautifulSoup(
        html.content,
        "lxml",
        from_encoding='utf-8')  # 获取lxml树
    urls = soup.find_all('a', attrs={'class': 'title'})  # 获取a标签，类名为title
    print(len(urls))
    for url in urls:
        lst = []
        b = 'https:' + url.get('href')
        print(b)
        lst.append(b)
        dts.append(lst)
    df = pd.DataFrame(dts, columns=['urls'])
df.to_excel(a + '.xlsx', encoding='utf-8')
end = time.time()
print("总共耗时：%f" % (end - start))
import  requests
import  re
from lxml import  etree
from fake_useragent import  UserAgent
import time
#总之就是非常可爱目前下载到第八话，来自轻之国度，第8话已经下载
headers = {
    "User-Agent": "UserAgent().firefox"
}
# base_url = "https://www.lightnovel.cn/search.php?mod=forum&searchid=6672&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=2"
# respnose = requests.get(base_url)   13 https://www.lightnovel.cn/thread-929821-1-1.html
# e = etree.HTML(respnose.text)     14   https://www.lightnovel.cn/thread-930280-1-1.html
url ="https://www.lightnovel.cn/thread-927807-1-1.html"
# url = [
#     "https://www.lightnovel.cn/thread-919898-1-1.html",
#     "https://www.lightnovel.cn/thread-920546-1-1.html",
#     "https://www.lightnovel.cn/thread-922043-1-1.html",
#     "https://www.lightnovel.cn/thread-922815-1-1.html",
#     "https://www.lightnovel.cn/thread-924380-1-1.html"
# ]
i = 0
respnose = requests.get(url)
print(respnose.text)
e = etree.HTML(respnose.text)
imgs_url = e.xpath('//img[@class="zoom"]/@file')
for img_url in imgs_url :
        response = requests.get(img_url)
        img_name = str(i)+'.jpg'
        print(img_name+"下载中........")
        with open("第"+img_name, 'wb') as f:
            f.write(response.content)
        print(img_name + "下载ok........")
        i = i + 1



# 总之就是非常可爱爬虫，目前抓取到87话

import  requests
import  time
from  lxml import etree
from fake_useragent import  UserAgent
from selenium import  webdriver
# 待更新url
url = "https://www.43423.cc/chapter/255959"
driver = webdriver.Firefox()
driver.get(url)
index = 0
info = driver.page_source
e = etree.HTML(info)
base_num = e.xpath("//select/option")
num = len(base_num)
driver.implicitly_wait(30)
i = 0


while (True):
        img_url = e.xpath("//img[@class='comicimg']/@src")  # list元素
        img = ''.join(img_url)  # list元素转字符串
        response = requests.get(img)
        img_name = str(index) + (".jpg")
        print(img_name)
        print(img_name + "下载中........")
        with open("第" + img_name, 'wb') as f:
            f.write(response.content)
        print(img_name + "下载ok........")
        index = index+1
        time.sleep(1)
        if(i<num-1):
            element =  driver.find_element_by_link_text("下一页")
            element.click()
            info = driver.page_source
            e = etree.HTML(info)
            i = i+1
        else :
            element = driver.find_element_by_link_text("下一章")
            element.click()
            info = driver.page_source
            e = etree.HTML(info)
            base_num = e.xpath("//select/option")
            num = len(base_num)
            print(num)
            i = 0

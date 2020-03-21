import  requests
import  time
from  lxml import etree
from fake_useragent import  UserAgent
from selenium import  webdriver
# 待更新url
url = "http://www.1kkk.com/ch1-651511"
driver = webdriver.Firefox()
headers = {
    "User-Agent": "UserAgent().firefox"
}
driver.get(url)
index = 0
info = driver.page_source
e = etree.HTML(info)

driver.implicitly_wait(30)
while True:
    img_url = e.xpath("//img[@id='cp_image']/@src")  # list元素
    img = ''.join(img_url)  # list元素转字符串
    print(img)
    response = requests.get(img)
    img_name = str(index) + (".jpg")
    print(img_name)
    print(img_name + "下载中........")
    with open("第" + img_name, 'wb') as f:
        f.write(response.content)
    print(img_name + "下载ok........")
    index = index + 1
    time.sleep(1)
    ele = driver.find_element_by_link_text("下一页")
    ele.click()
    info = driver.page_source
    e = etree.HTML(info)
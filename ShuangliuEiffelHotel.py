import  requests
import  re
from lxml import  etree
from fake_useragent import  UserAgent
import time
from selenium import  webdriver

url = "http://hotels.huazhu.com/hotel/detail/6100311?CheckInDate=2020-01-06&CheckOutDate=2020-01-07"
headers = {
    "User-Agent": "UserAgent().firefox"
}
driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)
info = driver.page_source
e = etree.HTML(info)
roomType = e.xpath('//tr[@class="room first"]//h3/text()')

numType = len(roomType)
imageType = e.xpath('//div[@class="floatimage"]//img/@src')
# imaggNum = len(imageType)
# print(imageType)
# driver.quit()
trueInfo = e.xpath('//div[@class="roominfobox-table-box"]//tr/td/text()')
numTrueInfo  = (len(trueInfo)) / 8
f = open("hanTing.txt", 'a+',encoding='utf-8')
k = 0


for i in range(0,numType):
    f.write(roomType[i])
    f.write("\n")
    f.write("图片地址：") # if(k<=5):
    #      f.write(imageType[k])
    #      f.write("\n")
    #      k = k+1

    for j in  range(0,8):
        f.writelines(trueInfo[j])
        f.write("  ")
    f.write("\n")
driver.quit()
print("sss")





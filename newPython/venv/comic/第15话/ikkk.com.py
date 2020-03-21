import  requests
import  time
from  lxml import etree
from fake_useragent import  UserAgent
from selenium import  webdriver

url = "http://www.1kkk.com/ch1-651511/"
driver = webdriver.Firefox()
driver.get(url)
index = 0
info = driver.page_source
e = etree.HTML(info)
base_num = e.xpath("//select/option")
num = len(base_num)
driver.implicitly_wait(30)
i = 0
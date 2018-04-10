#!/usr/bin/python3
###自动登录OA
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import re
'''
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://192.168.1.90:8080/login/Login.jsp') 
'''
driver = webdriver.Chrome()
driver.get("http://192.168.1.90:8080/login/Login.jsp")
print("正在输入账号")
time.sleep(2)
elem = driver.find_element_by_id("loginid")
elem.send_keys("SH17032801")
print("正在输入密码")
time.sleep(1)
elem2 = driver.find_element_by_id("userpassword")
elem2.send_keys("11111111")
elem.send_keys(Keys.RETURN)
print("模拟点击确定")
time.sleep(3)
###若重复登录OA需要此动作_ButtonCancel_1518077387367
# elem6_id=re.findall(r'^_ButtonCancel_\d*',driver.page_source)
# print(elem6_id)
# print(driver.page_source)
# g=open("c:/users/administrator/desktop/22.txt","wb")
# g.write(driver.page_source)
# g.close()
# try:
#     elem6 = driver.find_element_by_id(elem6_id[0])
#     elem6.send_keys(Keys.RETURN)
#     elem3=driver.find_element_by_id("_ButtonCancel_1518076039172")
#     elem3.send_keys(Keys.RETURN)
#     elem4=driver.find_element_by_id("_ButtonOK_1518076039202")
#     elem.send_keys(Keys.RETURN)
#     print("模拟点击确定")
#     time.sleep(2)
#     elem5=driver.find_element_by_id("_ButtonCancel_1518076599463")
#     elem5.send_keys(Keys.RETURN)
# except:
#     print("运转正常")

cookies = driver.get_cookies()
print(cookies[0])
headers={"Host":"192.168.1.90:8080",
         "Referer":"http://192.168.1.90:8080/wui/theme/ecology8/page/login.jsp?emplateId=12&logintype=1&gopage=&languageid=7&message=16",
         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
         "cookies":cookies[0],
        }
session = requests.session()

Oa_url='http://192.168.1.90:8080/workflow/request/ViewRequest.jsp?'
data={"requestid":"338212","_workflowid":"44"}
response = session.get(Oa_url,data=data,cookies=cookies[0])
print(response.status_code)
f=open("C:/users/administrator/desktop/11.html","wb")
f.write(response.content)
f.close()
session.close()
# print(driver.page_source)
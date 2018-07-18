"""
-------------------------------------------------
   File Name：     05-AutoAddFans
   Description :   在知乎上自动互粉
   Author :       gaox
   date：          7/18/18
-------------------------------------------------
   Change Activity:
                   7/18/18:
-------------------------------------------------
"""
__author__ = 'gaox'

# cookie 登录

from selenium import webdriver
import time

def start_chrome():
    driver = webdriver.Chrome('../0-Additionals/chromedriver')
    driver.start_client()
    return driver

def find_strangers():
    btn_sel = 'div.ContentItem-extra > button.Button--blue'
    elms = driver.find_elements_by_css_selector(btn_sel)
    return elms


username = 'None'
url = 'www.zhihu.com'
follower_url = 'http://zhihu.com/people/{}/followers'.format(username)
driver = start_chrome()
driver.get(url)
time.sleep(20)  # wait for log in
driver.get(follower_url)
time.sleep(6)   # wait for loading

strangers = find_strangers()
for s in strangers:
    s.click()       # 模拟js的单击操作


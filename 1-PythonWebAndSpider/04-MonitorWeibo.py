"""
-------------------------------------------------
   File Name：     04-MonitorWeibo
   Description :
   Author :       gaox
   date：          7/18/18
-------------------------------------------------
   Change Activity:
                   7/18/18:
-------------------------------------------------
"""
__author__ = 'gaox'

import time
import requests
from selenium import webdriver


url = 'https://weibo.com/2803301701/GqbhzyZuU?from=page_1002062803301701_profile&wvr=6&mod=weibotime&type=comment'

def start_chrome():
    driver = webdriver.Chrome(executable_path='../0-Additionals/chromedriver')
    driver.start_client()
    return driver

def find_info():
    ele_pos = 'span.pos > span > span > em:nth-child(2)'
    eles = driver.find_elements_by_css_selector(ele_pos)
    return eles


def make_message(info):
    requests.post(
        "https://api.alertover.com/v1/alert",
        data={
            "source": "s-b95c7d87-67f0-476d-bbe9-8b7866df",
            "receiver": "g-6285daf4-4f68-4869-a212-09aa1b07",
            "content": "Comments is more than {}".format(info[2].text),
            "title": "Comments Alert"
        }
    )

def push_it(info):
    make_message(info)

if __name__=='__main__':
    driver = start_chrome()
    driver.get(url)
    time.sleep(6)
    info = find_info()
    repo, comt, star = [int(x.text) for x in info[1:]]
    print(f'repo is {repo}')
    print(f'comt is {comt}')
    print(f'star is {star}')

    while True:
        if comt > 20000:
            push_it(info)
            break
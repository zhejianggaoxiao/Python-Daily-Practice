"""
-------------------------------------------------
   File Name：     041-NotifyOscar
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


url = 'https://s.weibo.com/weibo/%2523%25E5%25A5%25A5%25E6%2596%25AF%25E5%258D%25A1%2523&Refer=STopic_box'

def start_chrome():
    driver = webdriver.Chrome(executable_path='../0-Additionals/chromedriver')
    driver.start_client()
    return driver

def find_info():
    ele_pos = 'div.info > p.total > span'
    eles = driver.find_elements_by_css_selector(ele_pos)
    return eles[:2]


def make_message(read):
    requests.post(
        "https://api.alertover.com/v1/alert",
        data={
            "source": "s-b95c7d87-67f0-476d-bbe9-8b7866df",
            "receiver": "g-6285daf4-4f68-4869-a212-09aa1b07",
            "content": "Comments is more than {}".format(read),
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
    read, comt= info[0].text[2:], info[1].text[2:]
    if read[-1]=='万':
        read = float(read[:-1])*10**8
    elif read[-1]=='亿':
        read = float(read[:-1]) * 10 ** 12

    if comt[-1]=='万':
        comt = float(comt[:-1])*10**8
    elif read[-1]=='亿':
        comt = float(comt[:-1]) * 10 ** 12

    print(f'repo is {read}')
    print(f'comt is {comt}')


    while True:
        if comt > 350*10**8:
            push_it(comt)
            break
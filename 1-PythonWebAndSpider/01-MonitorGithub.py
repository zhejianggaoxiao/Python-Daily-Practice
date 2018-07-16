"""
-------------------------------------------------
   File Name：     01-MonitorGithub
   Description :  监测特定Github更新并打开网址
   Author :       gaox
   date：          7/16/18
-------------------------------------------------
   Change Activity:
                   7/16/18:
-------------------------------------------------
"""
__author__ = 'gaox'


# api   https://api.github.com/repos/zhejianggaoxiao/Pretty_Codes
# www   https://github.com/zhejianggaoxiao/Pretty_Codes

import requests
import webbrowser
import time

api = 'https://api.github.com/repos/zhejianggaoxiao/Pretty_Codes'
web_page = 'https://github.com/zhejianggaoxiao/Pretty_Codes'

last_update = None
all_info = requests.get(api).json()
cur_update = all_info['updated_at']
print(cur_update)

while True:
    if not last_update:
        last_update = cur_update

    if last_update<cur_update:
        webbrowser.open(web_page)

    time.sleep(600)

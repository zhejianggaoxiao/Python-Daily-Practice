"""
-------------------------------------------------
   File Name：     01.1-StarAndOpen
   Description :
   Author :       gaox
   date：          7/16/18
-------------------------------------------------
   Change Activity:
                   7/16/18:
-------------------------------------------------
"""
__author__ = 'gaox'

import requests
import webbrowser

api = 'https://api.github.com/users/zhejianggaoxiao/starred'

all_repos = requests.get(api).json()

repos = []

for repo in all_repos:
    repos_info = {}
    repos_info['name'] = repo['name']
    repos_info['url'] = repo['owner']['html_url']
    repos.append(repos_info)

for item in repos:
    webbrowser.open(item['url'])

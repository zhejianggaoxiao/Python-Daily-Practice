"""
-------------------------------------------------
   File Name：     021-FindRepos
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
from datetime import datetime, timedelta
api = 'https://api.github.com/search/repositories?q=language:{}+size:{}+created:>{}'

from_date = (datetime.now()-timedelta(7)).strftime('%Y-%m-%d')

lang = 'python'
size = '<200'

repos = requests.get(api.format(lang, size, from_date)).json()['items']


repos_info = []
for repo in repos:
    item = {}
    item['name'] = repo['name']
    item['url'] = repo['html_url']
    repos_info.append(item)

print(repos_info[:], len(repos_info))


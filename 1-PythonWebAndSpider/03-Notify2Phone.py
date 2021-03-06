"""
-------------------------------------------------
   File Name：     03-Notify2Phone
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

def get_repos_info():
    api = 'https://api.github.com/search/repositories?q=topic:{topic}+language:{lang}+created:{date}'
    topic = 'crawler'
    lang = 'python'
    date = (datetime.now()-timedelta(7)).strftime('%Y-%m-%d')
    repos_info = requests.get(api.format(topic=topic, lang=lang, date=date)).json()['items']
    if repos_info:
        repos = []
        for repo in repos_info:
            item = {}
            item['name'] = repo['name']
            item['url'] = repo['html_url']
            repos.append(item)
        return repos
    else:
        return 'None'

def make_message(repos):
    if repos=='None':
        return 'No Date Found'
    else:
        for item in repos:
            requests.post(
                "https://api.alertover.com/v1/alert",
                data={
                    "source": "s-b95c7d87-67f0-476d-bbe9-8b7866df",
                    "receiver": "g-6285daf4-4f68-4869-a212-09aa1b07",
                    "content": "name:{}, url:{}".format(item['name'],item['url']),
                    "title": "{}".format(item['name'])
                }
            )

def push_it(repos):
    make_message(repos)

repos = get_repos_info()
push_it(repos)

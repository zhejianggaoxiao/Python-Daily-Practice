"""
-------------------------------------------------
   File Name：     02-CompData
   Description :  比较不同仓库的数据（包括fork，star以及生态数据）
   Author :       gaox
   date：          7/16/18
-------------------------------------------------
   Change Activity:
                   7/16/18:
-------------------------------------------------
"""
__author__ = 'gaox'

import requests

def get_names():
    names = input('请输入需要比较的仓库，以空格分隔：')
    return names.split()

def check_repos(names):
    # star 和 fork 的数据
    api = 'https://api.github.com/search/repositories?q='
    # 生态数据
    ecosys_api = 'https://api.github.com/search/repositories?q=topic:'

    for name in names:
        repo_info = requests.get(api+name).json()['items'][0]

        stars = repo_info['stargazers_count']
        forks = repo_info['forks_count']

        eco_counts = requests.get(ecosys_api+name).json()['total_count']

        print(name)
        print(stars)
        print(forks)
        print(eco_counts)
        print('--------------')

names = get_names()
check_repos(names)
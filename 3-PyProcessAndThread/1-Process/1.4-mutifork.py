"""
-------------------------------------------------
   File Name：     1.4-mutifork
   Description :
   Author :       gaox
   date：          7/27/18
-------------------------------------------------
   Change Activity:
                   7/27/18:
-------------------------------------------------
"""
__author__ = 'gaox'


import os

pid = os.fork()

if pid==0:
    print("process 1")
else:
    print("process 2")

pid = os.fork()

if pid==0:
    print("process 3")
else:
    print("process 4")
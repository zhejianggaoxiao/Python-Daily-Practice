"""
-------------------------------------------------
   File Name：     1.3-forkandglobals
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
import time

num = 0

pid = os.fork()

if pid==0:
    num+=1
    print("This is child prosecc, the num = %s" %num)
else:
    time.sleep(1)
    num += 1
    print("This is father prosecc, the num = %s" % num)
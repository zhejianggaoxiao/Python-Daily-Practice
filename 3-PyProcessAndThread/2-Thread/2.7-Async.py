"""
-------------------------------------------------
   File Name：     2.7-Async
   Description :
   Author :       gaox
   date：          7/28/18
-------------------------------------------------
   Change Activity:
                   7/28/18:
-------------------------------------------------
"""
__author__ = 'gaox'

from multiprocessing import Pool

import time
import os

def test():
    print(f"--- 进程池中的进程 --- pid = {os.getpid()}, ppid = {os.getppid()}")
    for i in range(3):
        print(f"--- {i} ---")
        # time.sleep(1)
    return "hahah"

def test2(args):
    print(f"--- callback func --- pid = {os.getpid()}")
    print(f"--- callback func --- args = {args}")

pool = Pool(3)
pool.apply_async(func=test, callback=test2)
# pool.apply_async(func=test, callback=test2)


# pool.close()
# pool.join()

# time.sleep(5)

print(os.getpid())
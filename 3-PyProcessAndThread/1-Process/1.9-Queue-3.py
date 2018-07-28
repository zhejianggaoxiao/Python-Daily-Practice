"""
-------------------------------------------------
   File Name：     1.9-Queue-3
   Description :
   Author :       gaox
   date：          7/28/18
-------------------------------------------------
   Change Activity:
                   7/28/18:
-------------------------------------------------
"""
__author__ = 'gaox'

from multiprocessing import Manager, Pool

import os, time, random

def reader(q):
    print(f"reader({os.getpid()}) start, father process({os.getppid()})")
    while True:
        if not q.empty():
            print(f"reader get: {q.get()}")


def writer(q):
    print(f"writer({os.getpid()}) start, father process({os.getppid()})")
    for i in "Python":
        q.put(i)
        print(f"writer put: {i}")
        time.sleep(random.random())

if __name__ =="__main__":
    print(f"({os.getppid()}) starts")
    q = Manager().Queue()
    p = Pool()

    p.apply_async(writer,(q,))
    p.apply_async(reader,(q,))

    p.close()
    p.join()
    print("*"*20)


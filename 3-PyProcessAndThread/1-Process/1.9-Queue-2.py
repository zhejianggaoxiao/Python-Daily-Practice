"""
-------------------------------------------------
   File Name：     1.9-Queue-2
   Description :
   Author :       gaox
   date：          7/28/18
-------------------------------------------------
   Change Activity:
                   7/28/18:
-------------------------------------------------
"""
__author__ = 'gaox'

from multiprocessing import Process, Queue

import os, time, random

def write(q):
    for val in ['A', 'B', 'C']:
        print(f"Put {val} to queue ...")
        q.put(val)
        time.sleep(random.random())


def read(q):
    while True:
        if not q.empty():
            val = q.get(True)
            print(f"Get {val} from queue ...")
            time.sleep(random.random())
        # else:
        #     break

if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    # pw.join()
    # pr.join()

    print("*"*20)




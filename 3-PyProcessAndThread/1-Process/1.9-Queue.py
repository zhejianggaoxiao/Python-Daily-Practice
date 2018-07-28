"""
-------------------------------------------------
   File Name：     1.9-Queue
   Description :
   Author :       gaox
   date：          7/27/18
-------------------------------------------------
   Change Activity:
                   7/27/18:
-------------------------------------------------
"""
__author__ = 'gaox'

from multiprocessing import  Queue

q = Queue(3)

q.put(1)
q.put(2)
print(q.full())
q.put(3)
print(q.full())


try:
    q.put(4, True, 2)
except Exception:
    print("队列已满")

try:
    q.put_nowait(4)
except:
    print("队列已满" )


# if not q.full():
q.put_nowait(4)

if not q.empty():
    for i in range(3):
        print(q.get_nowait())
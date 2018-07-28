"""
-------------------------------------------------
   File Name：     1.8-Poll
   Description :
   Author :       gaox
   date：          7/27/18
-------------------------------------------------
   Change Activity:
                   7/27/18:
-------------------------------------------------
"""
__author__ = 'gaox'

from multiprocessing import Pool

import os, time, random

def worker(msg):
    t_start = time.time()
    print("%s 开始执行，进程号为 %s" %(msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时 %0.2f" %(t_stop-t_start))

p = Pool(3)

for i in range(0,10):
    # p.apply(worker,(i,))
    p.apply_async(worker, (i,))

print("---- start ----")
p.close()
# time.sleep(1)
# p.terminate()
p.join()
print("---- end ----")
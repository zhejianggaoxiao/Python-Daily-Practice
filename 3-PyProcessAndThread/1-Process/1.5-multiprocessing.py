"""
-------------------------------------------------
   File Name：     1.5-multiprocessing
   Description :
   Author :       gaox
   date：          7/27/18
-------------------------------------------------
   Change Activity:
                   7/27/18:
-------------------------------------------------
"""
__author__ = 'gaox'

from multiprocessing import Process

import os, time

def run_proc(args, **kwargs):
    print("子进程运行中，name = %s, pid = %s" %(args, os.getpid()))
    print(kwargs)
    for i in range(3,0,-1):
        print('%s ....' %i)
        time.sleep(1)
    print(os.getppid())

if __name__ == "__main__":
    print("父进程 %s" %os.getpid())
    p = Process(target=run_proc, args=('test',), kwargs={"lucky":1000})
    print("子进程将要执行")
    p.start()
    # p.join()
    # time.sleep(1)
    # p.terminate()
    print("子进程别名 %s" %p.name)
    print("子进程id %s" %p.pid)
    print("子进程已结束")
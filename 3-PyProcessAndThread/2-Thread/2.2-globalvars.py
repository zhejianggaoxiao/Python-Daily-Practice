"""
-------------------------------------------------
   File Name：     2.2-globalvars
   Description :
   Author :       gaox
   date：          7/28/18
-------------------------------------------------
   Change Activity:
                   7/28/18:
-------------------------------------------------
"""
__author__ = 'gaox'

from threading import Thread, Lock
import time, random

g_num = 100

def work1(lock):
    global g_num

    for i in range(1000000):
        lock.acquire()
        g_num  +=1
        lock.release()
        # time.sleep(random.random())
    print(f"in work1, g_num is {g_num}")




def work2(lock):
    global g_num
    for i in range(1000000):
        temp = lock.acquire()
        g_num -= 1
        lock.release()
        # time.sleep(random.random())
    print(f"in work2, g_num is {g_num}")


lock = Lock()

t1 = Thread(target=work1, args=(lock,))
t1.start()

# time.sleep(1)
t2 = Thread(target=work2,args=(lock,))

t2.start()

t1.join()
t2.join()

print("*"*20)
print(g_num)
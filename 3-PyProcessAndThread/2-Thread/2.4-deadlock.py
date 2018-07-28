"""
-------------------------------------------------
   File Name：     2.4-deadlock
   Description :
   Author :       gaox
   date：          7/28/18
-------------------------------------------------
   Change Activity:
                   7/28/18:
-------------------------------------------------
"""
__author__ = 'gaox'

import threading
import time

class MyThread1(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name+'----do1---up----')
            time.sleep(1)

            if mutexB.acquire():
                print(self.name+'----do1---down----')
                mutexB.release()
            mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name+'----do2---up----')
            time.sleep(1)
            if mutexA.acquire():
                print(self.name+'----do2---down----')
                mutexA.release()
            mutexB.release()

mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
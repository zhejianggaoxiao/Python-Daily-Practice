"""
-------------------------------------------------
   File Name：     2.1-thread-3
   Description :
   Author :       gaox
   date：          7/28/18
-------------------------------------------------
   Change Activity:
                   7/28/18:
-------------------------------------------------
"""
__author__ = 'gaox'

from threading import Thread
import time

class MyThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(f"id={self.name} ... msg...{i}")


if __name__ == "__main__":
    # t = MyThread()
    # t.start()

    for i in range(5):
        t = MyThread()
        t.start()
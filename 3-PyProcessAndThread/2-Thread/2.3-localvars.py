"""
-------------------------------------------------
   File Name：     2.3-localvars
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
import  time

class MyThread(Thread):

    def __init__(self, num, sleepTime):
        super().__init__()
        self.num = num
        self.sleepTime = sleepTime

    def run(self):
        self.num+=1
        time.sleep(self.sleepTime)
        print(f"线程({self.name}), num={self.num}")

if __name__ == "__main__":
    t1 = MyThread(100,5)
    t1.start()
    t2 = MyThread(200,1)
    t2.start()

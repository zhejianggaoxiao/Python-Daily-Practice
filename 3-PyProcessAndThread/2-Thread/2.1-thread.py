"""
-------------------------------------------------
   File Name：     2.1-thread
   Description :
   Author :       gaox
   date：          7/28/18
-------------------------------------------------
   Change Activity:
                   7/28/18:
-------------------------------------------------
"""
__author__ = 'gaox'


from  threading  import Thread

import time
def print1():
    for i in range(4):
        print(i)
        time.sleep(1)

def saySorry():
    print("I'm so sorry")
    time.sleep(1)

if __name__=="__main__":

    t0 = Thread(target=print1)
    t0.setDaemon(True)
    t0.start()

    for i in range(6):
        t = Thread(target=saySorry)

        t.start()

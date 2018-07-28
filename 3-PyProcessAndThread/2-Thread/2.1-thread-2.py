"""
-------------------------------------------------
   File Name：     2.1-thread-2
   Description :
   Author :       gaox
   date：          7/28/18
-------------------------------------------------
   Change Activity:
                   7/28/18:
-------------------------------------------------
"""
__author__ = 'gaox'

from threading import Thread, enumerate

from time import sleep, time

def sing():
    for i in range(3):
        print("Singing ... %s" %i)
        sleep(1)


def dance():
    for i in range(3):
        print("Dancing ... %s" %i)
        sleep(0.7)


if __name__=="__main__":
    print("--- Start ----")

    t1 = Thread(target=sing)
    t2 = Thread(target=dance)
    t2.s

    t1.start()
    t2.start()

    for i in enumerate():
        print(i)


    while True:
        length = len(enumerate())
        print("当前线程数：%s" %length)
        if length<=1:
            break

        sleep(0.5)
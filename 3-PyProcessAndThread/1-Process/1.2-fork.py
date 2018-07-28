"""
-------------------------------------------------
   File Name：     1.2-fork
   Description :
   Author :       gaox
   date：          7/27/18
-------------------------------------------------
   Change Activity:
                   7/27/18:
-------------------------------------------------
"""
__author__ = 'gaox'

import os

pid = os.fork()

if pid==0:
    print("This is child process %s" %os.getpid())
    print("My father id is %s" %os.getppid())
else:
    print("This is father process")
    print("The  father process id is %s" % os.getpid())
    print("The child process id is %s" %pid)
    print("*"*20)
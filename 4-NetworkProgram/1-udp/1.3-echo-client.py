"""
-------------------------------------------------
   File Name：     1.3-echo-client
   Description :
   Author :       gaox
   date：          7/29/18
-------------------------------------------------
   Change Activity:
                   7/29/18:
-------------------------------------------------
"""
__author__ = 'gaox'

import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr=('', 8899)

n=0
while n<10:
    client.sendto(b"hello world", addr)
    time.sleep(1)
    n+=1


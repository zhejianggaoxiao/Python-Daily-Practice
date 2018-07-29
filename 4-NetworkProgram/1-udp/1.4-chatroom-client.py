"""
-------------------------------------------------
   File Name：     1.4-chatroom-client
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
import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr=('', 8899)

while True:
    stat = input(f"[ C - {datetime.datetime.now()}]:")
    if stat == 'bye':
        break
    client.sendto(stat.encode("utf-8"), addr)

client.close()
"""
-------------------------------------------------
   File Name：     1.4-chatroom-server
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

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("", 8899))

while True:

    data = server.recvfrom(1024)
    print(f"[ S - {datetime.datetime.now()}]: {data[0]}")

server.close()


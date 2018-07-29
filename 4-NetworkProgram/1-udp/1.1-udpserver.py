"""
-------------------------------------------------
   File Name：     1.1-udpserver
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

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = ("127.0.0.1", 8080)

server.bind(addr)

while True:

    recData = server.recvfrom(1024)
    print(recData)
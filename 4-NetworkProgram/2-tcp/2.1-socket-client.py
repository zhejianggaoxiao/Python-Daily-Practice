"""
-------------------------------------------------
   File Name：     2.1-socket-client
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

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('', 9090)

client.connect(addr)

client.send("hello".encode("utf-8"))
data = client.recv(1024)
print(data.decode("utf-8"))
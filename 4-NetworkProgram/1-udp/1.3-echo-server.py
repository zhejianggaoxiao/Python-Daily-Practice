"""
-------------------------------------------------
   File Name：     1.3-echo-server
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

server.bind(("", 8899))

n=1
while True:

    data = server.recvfrom(1024)
    server.sendto(data[0],data[1])

    print(f"这是第{n}次数据发送：{data}")
    n+=1

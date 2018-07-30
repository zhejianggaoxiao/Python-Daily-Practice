"""
-------------------------------------------------
   File Name：     2.1-socket-server
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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('', 9090)
server.bind(addr)

server.listen(3)

conn, addr = server.accept()

data = conn.recv(1024)
print(data.decode("utf-8"))


conn.send('thank you'.encode("utf-8"))

conn.close()

server.close()


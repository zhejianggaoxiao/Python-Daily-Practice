"""
-------------------------------------------------
   File Name：     1.2-udpclient
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

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = ("127.0.0.1", 8080)


client.sendto("helllo".encode("utf-8"),addr)

"""
-------------------------------------------------
   File Name：     1.5-thread_chat
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
from threading import Thread

client_server = None

def recv(server):
    global client_server
    while True:
        recvData = server.recvfrom(1024)
        if recvData:
            # print(f"[{datetime.datetime.now()} - Client]:{recvData[0].decode('utf-8')}")
            print(recvData[0].decode('utf-8'))
            client_server = recvData[1]


def send(server):
    global client_server
    while True:
        if client_server:
            # stat = input(f"[{datetime.datetime.now()} - Server]:")
            stat = input()
            server.sendto(stat.encode("utf-8"), client_server)
            # print(f"[{datetime.datetime.now()} - Server]:{stat}")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('',9999))

    tr = Thread(target=recv, args=(server,))
    ts = Thread(target=send, args=(server,))
    tr.start()
    ts.start()

    tr.join()
    ts.join()



if __name__=="__main__":
    main()



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

addr = ('',9999)

def recv(client):
    while True:
        recvData = client.recvfrom(1024)
        if recvData:
            # print(f"[{datetime.datetime.now()} - Server]:{recvData[0].decode('utf-8')}")
            print(recvData[0].decode('utf-8'))


def send(client):
    while True:
        # stat = input(f"[{datetime.datetime.now()} - Client]:")
        stat = input()
        client.sendto(stat.encode("utf-8"), addr)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    tr = Thread(target=recv, args=(client,))
    ts = Thread(target=send, args=(client,))
    tr.start()
    ts.start()

    tr.join()
    ts.join()


if __name__ == "__main__":
    main()



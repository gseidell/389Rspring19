#!/usr/bin/env python3

import hashlib
import string
import socket
import time

f= open("../passwords.txt","r")
passwords = f.readlines()
passwords = [a[0:-1] for a in passwords]
f.close()
characters = string.ascii_lowercase

def crack(h):
    for c in characters:
        for p in passwords:
            if hashlib.sha256((c+p).encode()).hexdigest() == h:
                return c+p+"\n"


def server_crack():
    
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    for i in range(3):
        data = s.recv(4096)
        print(data.decode())
        ans = crack(data.decode().split("\n")[2])
        print(ans)
        print(s.send(ans.encode()))

    data = s.recv(1024)
    print(data)


if __name__ == "__main__":
    server_crack()

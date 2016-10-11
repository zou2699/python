#!/usr/bin/env python
# encoding: utf-8

import socket

host,port = '192.168.42.142',9001
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((host,port))

while True:
    user_input = raw_input("msg to send:").strip()
    if len(user_input) == 0:continue
    c.send(user_input)

    return_data = c.recv(1024)
    print "Receved:",return_data
c.close()

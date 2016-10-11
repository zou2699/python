#!/usr/bin/env python
# encoding: utf-8

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '192.168.42.142'
port = 9001

s.bind((host,port))
s.listen(1)
conn,addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:break
    print 'Get connection from',addr,data
    conn.send('Thank you for connecting,%s' % data)
conn.close()

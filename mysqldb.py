#!/usr/bin/env python
# encoding: utf-8

import MySQLdb

conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = 'z',port = 3306,db = 'mysql')
cur = conn.cursor()
cur.execute('show tables')
qur_result = cur.fetchall()

for record in qur_result:
    print record

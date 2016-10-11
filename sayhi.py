#!/usr/bin/env python
# encoding: utf-8

#装饰器例子
import time

def time_counter(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print 'This function costs :', end -start
    return wrapper

@time_counter
def sayHi():
    today = time.ctime()
    print 'Hello Google,today is %s' % today

sayHi()



'''
#等同于@time_counter
sayHi = time_counter(sayHi)
sayHi()
'''

#!/usr/bin/env python
# encoding: utf-8

class Person:
    def __init__(self,name,age):#构造函数，调用后立即执行
        print 'init'
        self.Name = name
        self.Age = age

    def sayHi(self):
        print 'Hi,my name is %s,I am %s years old' % (self.Name,self.Age)
        self.__talk()

    def __del__(self):#析构函数，内存释放前执行
        print 'I got killed just now...bye',self.Name

    def __talk(self):#私有属性，不能外表调用
        print 'I am private'

p = Person('zou',22)
p.sayHi()
#调用私有属性 p.Person__talk()
p._Person__talk()

#释放内存
print "释放内存"
del p
print '*'*60

p2 = Person('zhl',22)
p2.sayHi()
print "程序退出"

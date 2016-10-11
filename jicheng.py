#!/usr/bin/env python
# encoding: utf-8

class SchoolMember:
    def __init__(self,name,gender,nationality = 'CN'):
        self.name = name
        self.gender = gender
        self.nation = nationality
    def tell(self):
        print 'Hi,my name is %s, I am from %s' % (self.name,self.nation)


class Student(SchoolMember):
    def __init__(self,Name,Gender,Class,Score,Nation = 'US'):
        SchoolMember.__init__(self,Name,Gender,Nation)
        self.Class = Class
        self.Score = Score
    def payTuition(self,amount):
        if amount < 6499:
            print 'Get the fuck off..'
        else:
            print 'Wlecome onboard!'


class Teacher(SchoolMember):
    def __init__(self,Name,Gender,Course,Salary,Nation = 'US'):
        SchoolMember.__init__(self,Name,Gender,Nation)
        self.Course = Course
        self.Salary = Salary
    def teach(self):
        print 'I am teaching %s, I am making %d per month !' % (self.Course,self.Salary)

S1 = Student('zzz','male','Python','A+','CN')
S1.tell()
S1.payTuition(6500)
print '#'*40
S2 = Student('ttt','male','Python','A+')
S2.tell()
S2.payTuition(5500)

print '#'*40
T1 = Teacher('yang','female','Python',5000)
T1.tell()
T1.teach()

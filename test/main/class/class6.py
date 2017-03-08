#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#父类、子类
#或者叫：基类、派生类

class Father(object):
    def __init__(self):
        self.Fname = 'father'
        print 'father __init__'
    def Func(self):
        print 'father func'
    def Bad(self):
        print '坏习惯：抽烟喝酒'
        
class Son(Father):
    def __init__(self):
        self.Sname = 'son'
        print 'Son __init__'
        Father.__init__(self)  #显式调用父类的构造函数。不显式调用，则默认不会调用父类的构造函数，父类不必继承object类（经典类）
        super(Son, self).__init__()  #利用super函数调用父类构造函数，父类必须继承object类（新式类）
    def Bar(self):
        print 'son bar'
    def Bad(self):  #重写父类的方法
        print '坏习惯：抽烟'
        
        
s1 = Son()
s1.Bar()
s1.Func()

s1.Bad()



'''
经典类和新式类：
  python2.2之前，一直用的都是经典类。
    推荐用新式类。
    新式类是对经典类的扩展和修复某些bug，如增加__name__,__file__等，禁止访问类中的静态字段等等

'''
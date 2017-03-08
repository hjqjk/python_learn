#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#新式类：修复经典类的bug
#https://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html
#python3.0开始，经典类就被去掉了

#class A:  #经典类，基于深度优先算法，D类最终找到A类来继承save函数
class A(object):  #新式类，修复了经典类中的bug，找到最优，D类最终找到C类来继承save函数
    def __init__(self):
        print 'This is A'
    def save(self):
        print 'save method from A ~~'
    
class B(A):
    def __init__(self):
        print 'This is B'

class C(A):
    def __init__(self):
        print 'This is C'
    def save(self):
        print 'save method from C ~~'   
        
#注意多继承的顺序
class D(B,C):  #从左到右，继承于B和C，由于B没有save函数，按理应该去继承C的save函数
    def __init__(self):
        print 'This is D'
    
test = D()
test.save()  
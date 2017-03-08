#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#1. 类和对象(实例化)
#2. 静态字段、动态字段
#3. 静态方法（@staticmethod）、动态方法
#4. 特性()

class People:
    #静态字段，属于类，由类名调用。可修改。
    #Python中，静态字段是可以通过实例化对象访问的，但在其他语言中只能通过类名访问。静态字段加载到内存中，只会存一份
    Static_var = '人类'  
    
    def __init__(self,name,age): #初始化
        self.Name = name  #动态字段，属于对象
        self.Age = age
    
    #动态方法
    def Exercise(self): #动态方法，不能用类名调用
        print self.Age,self.Name
      
    #静态方法
    @staticmethod  
    def Foo():  #上面是Python自带的装饰器，加上这个就能标明这个函数是静态方法
        print "静态方法"
        
    #特性    
    @property
    def Character(self):  #将动态方法转为特性
        print self.Name
        return '特性'
    
user1 = People('hjq',25)  #创建对象，实例化。每创建一个对象，就都得开辟一次内存空间
user2 = People('jk',18)

print user1.Name   #对象名调用
print People.Static_var    #类名调用    
# print People.name #会报错。类不能访问动态字段
print user1.Static_var #对象可以访问类的静态字段
user1.Exercise()

People.Foo()  #只能用类名去调用静态方法

print user1.Character #对于特性，要使用对象名调用字段一样调用该方法
#print user1.Character() #会报错。

'''
注意：
    类中的方法能写成静态方法的最好写成静态方法。
    因为得实例化创建对象（开辟内存空间），才能用对象去调用动态方法。
    而静态方法可以直接用类名调用。
    尽量避免重复实例化创建对象的过程，因为每创建对象一次，就会开辟一次内存空间，对内存资源的消耗会加大。
'''

'''
Python的函数式编程(模块化)和面向对象编程的选择：
1、Python的设计理念是模块化，最初是没有面向对象的编程思想的，发展到后来，Python借鉴java的面向对象思想，支持面向对象编程。
2、下面两种编程的方法，都能避免因重复创建对象而导致的内存损耗，效果都是一样的：
    1）函数式编程（模块化编程），可通过 " 模块名.方法  " 方式访问
    2）面向对象编程，建立静态方法，通过 " 类名.静态方法 " 方式访问
   这两种编程方式都能用，不用拘泥于哪种更好的问题。实际上，Python中面向对象的静态方法，有点像鸡肋的存在。

'''

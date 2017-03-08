#!/usr/bin/env python
#_*_ coding:utf-8 _*_

# 抽象类 + 抽象方法 = 接口（第二种接口，即规范）

#接口
from abc import ABCMeta,abstractmethod
class Alert:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def send(self):
        pass
    
#Foo类继承于Alert接口，就必须实现接口定义的抽象方法，否则会报错
class Foo(Alert):
    def __init__(self):
        print '__init__'

#     def send(self):
#         print 'Foo send'

Foo().send()
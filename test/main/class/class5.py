#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#__init__、__del__、__call__

class People:
    def __init__(self): #构造函数
        pass
    
    def __del__(self):  #析构函数。当Python解析器要销毁没人用的对象时，会先调用析构函数，在执行销毁操作。
        print '解析器要销毁我啦，要做最后一次呐喊'
        
    def Go(self):
        print 'Go'
    
    def __call__(self):
        print 'call'

p1 = People()  #类名()调用 构造函数：__init__()
p1.Go()
p1()  #执行类的 __call__ 方法。对象名() Python会默认调用__call__方法，这是Python内部给你实现的。
People()()
#对象被销毁前，会先调用__del__方法
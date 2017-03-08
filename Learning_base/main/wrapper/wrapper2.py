#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#装饰器
#当调用装饰器对函数进行装饰，想对原函数调用前后进行修改，为方便自定义修改，传入两个函数参数

def Filter(before_func,after_func):
    def outer(main_func):
        def wrapper(arg1,arg2):
            before_result = before_func(arg1)  #调用原函数前的操作
            if before_result != None:
                return before_result #如果有返回，后边就不执行了
            
            main_result = main_func(arg1,arg2) #调用原函数
            if main_result != None:
                return main_result  #如果有返回，后边就不执行了
            
            after_result = after_func(arg2)  #调用原函数后的操作
            if after_result != None:
                return after_result
        return wrapper
    return outer

def before_func(arg):
    print 'before',arg
    #return 'B'
def after_func(arg):
    print 'after',arg
    return 'A'

@Filter(before_func, after_func) #传入函数引用
def func1(arg1,arg2):
    print 'main',arg1,arg2
    #return 'Main'
    
print func1('hello','python')


#装饰器也可以定义成一个类


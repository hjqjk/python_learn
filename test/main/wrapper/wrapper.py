#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#装饰器
#当你不清楚数据是怎么走动的时候，可以使用eclipse的断点功能查看
#利用断点调试，查看装饰器的函数调用和数据流动

def outer(func):  #形参：func ，实参：func1
    def wrapper(arg):  #从程序顺序来看，wrapper函数没有被调用前，会被先加载到内存.注意参数的
        func(arg)   #调用方法
        print '增加新的功能\n',arg
    return wrapper  #返回函数
    '''
    return wrapper，相当于：
        func1 = 
            def wrapper():  
                func()
                print '增加新的功能\n'
    '''
       
@outer   #将装饰器函数 和 该函数 联系起来，也可以这样理解：@outer = outer(func1)
def func1(arg):
    print "func1",arg
              
def func2():
    print "func2"
           
func1('hello python')
func2()

#在做web的权限控制的时候，可以使用到装饰器。
#如修改密码的过程：1、2、3、4 四步
#只有经过了1，才能到2，经过了2，才能到3...
#可在相应的装饰器上实现


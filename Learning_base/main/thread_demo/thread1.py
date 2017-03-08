#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from threading import Thread

def display(v1,v2,v3):
    print v1,v2,v3,'\n'

print 'before'    
t1 = Thread(target=display,args=(11,22,33,))  #创建一个线程，与函数display关联
t1.start()  #启动线程
print t1.getName()  #查看线程名

t2 = Thread(target=display,args=(111,222,333,))  #创建一个线程。通过Thread类的 run()方法调用display函数
t2.start()  #启动子线程，主线程不再管子线程了
print t2.getName()

print 'after'

#主线程按顺序执行
#子线程启动后，主线程不再管子线程的操作了。主线程和子线程互不干涉。

#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#自定义线程类

from threading import Thread
import time

class MyThread(Thread):
    def run(self):
        time.sleep(5)
        print '这是线程.'


def display(v1,v2,v3):
    for item in range(20):
        print item,
        time.sleep(0.5)  #睡眠0.5秒

print 'before'    
t1 = MyThread(target=display,args=(11,22,33,))  #创建一个线程

t1.start()  #启动线程


print 'after'

print '--- end ---'


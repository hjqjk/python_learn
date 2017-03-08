#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from threading import Thread
import time

def display(v1,v2,v3):
    for item in range(20):
        print item,
        time.sleep(0.5)  #睡眠0.5秒

print 'before'    
t1 = Thread(target=display,args=(11,22,33,))  #创建一个线程
print t1.isDaemon()  #默认为False,为False表示主线程会在完成所有操作后等待子线程完成操作才会退出
t1.setDaemon(True)  #为True表示，主线程完成操作后就会立即退出，不会再等子线程继续完成操作。主线程退出后，如果此时子线程还有操作没有完成，已经无法继续执行了。
t1.start()  #启动线程

t1.join(5)  #先执行5秒钟子线程的操作。5秒过后，执行主线程操作。

print 'after'

print '--- end ---'


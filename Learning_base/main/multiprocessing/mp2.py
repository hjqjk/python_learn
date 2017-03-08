#!/usr/bin/env python
#_*_ coding:utf-8 _*_


from multiprocessing import Process
import os

def info(title):
    print title
    print 'module name:',__name__
    
    if hasattr(os, 'getppid'):
        print 'parent process:',os.getppid()
    print 'process id:',os.getpid()
    
def f(name):
    info('function f')
    print 'hello',name
    
if __name__ == '__main__':
    info('main line')
    print '----------------'
    p = Process(target=f,args=('bob',))   #创建一个进程
    p.start()
    p.join()
    

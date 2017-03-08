#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#进程间同步数据：利用Lock来实现
from multiprocessing import Process
from multiprocessing import Lock

def f(l,i):
    #l.acquire()  #加锁
    print 'hello world',i
    #l.release()  #释放锁

if __name__ == '__main__':       
    lock = Lock()
    
    for num in range(10):
        Process(target=f,args=(lock,num)).start()
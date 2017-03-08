#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#进程间的内存同步方法：借用multiprocessing.Queue来实现
#multiprocessing.Queue 和 Queue是不一样的
from multiprocessing import Process
from multiprocessing import Queue

def f(q,n):
    q.put([n,'hello'])

if __name__ == '__main__':       
    q = Queue()  #队列
    for i in range(5):
        p = Process(target=f,args=(q,i)) #传入同一个Queue
        p.start()
        
    while True:
        print q.get()  #数据都加到同一个Queue
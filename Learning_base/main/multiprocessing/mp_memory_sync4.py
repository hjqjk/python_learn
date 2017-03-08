#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#通过第三方通道：Manager，实现进程间内存共享
#Manager支持类型： list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Queue, Value and Array
#Manager自身实现了线程安全，自身会管理锁

from multiprocessing import Process,Manager

def f(d,l):  #修改字典和列表
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()  #将列表反转
    
if __name__ == '__main__':
    manager = Manager()
    
    d = manager.dict()  #创建空字典
    l = manager.list(range(10)) #创建列表：[0,1,2,3,4,5,6,7,8,9]
     
    p = Process(target=f,args=(d,l)) #子进程，修改数据
    p.start()
    p.join()
    
    print d  #父进程，看得出数据被改变了
    print l
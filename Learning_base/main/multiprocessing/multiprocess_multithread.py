#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from multiprocessing import Pool
from threading import Thread
import os

#多进程多线程

def t_func(n):
    print 'threading,pid:%s --> %s' %(os.getpid(),n)

def p_func(x):
    for j in range(5):
        t = Thread(target=t_func,args=(j,))  #创建5个线程
        t.start()

if __name__ == '__main__':
    pool = Pool(processes=5)
    res_list = []  
    
    for i in range(10):
        res = pool.apply_async(p_func,[i])  #起10个进程
        print '---:',i
        res_list.append(res)
        
    for r in res_list:
        print r.get(timeout=1)  #获取结果
#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#多线程
from multiprocessing import Pool
import time


def f(x):
    time.sleep(0.5)
    return x*x

if __name__ == '__main__':
    
    #print map(f,[1,2,3,4,5,6,7])   #串型处理，花费时间长
    
    p = Pool(10)  #设定进程池，最多只能起5个进程
    print p.map(f,[1,2,3,4,5,6,7])  #并行处理，效率提高
#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#线程锁

import threading
import time

# num = 0  #全局变量
#  
# def run(n):
#     time.sleep(1)  
#     global num  #函数内不能直接使用全局变量，要用就必须用global指定
#     num += 1
#     print '%s\n' % num
#      
# for item in range(50): #起200个线程，去运行run函数对num变量+1，有可能会发生多个线程抢占num变量的结果，导致数据发生错乱
#     t = threading.Thread(target=run,args=(item,)) 
#     t.start()
#      
print '----------------------------'
    
num2 = 0
def run2(n):
    time.sleep(1)  
    global num2  
    lock.acquire()  #锁住，只有一个线程能操作
    num2 += 1
    lock.release()  #解锁
    print '%s\n' % num2

lock = threading.Lock()  #创建锁
 
for item in range(50): #起200个线程
    t2 = threading.Thread(target=run2,args=(item,)) 
    t2.start()
    
    
#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#线程锁：threading.BoundedSemaphore(4)
#即便锁住了，也允许同一时刻有多个线程进入
#实现实例：mysql的最大连接数，允许最多有多少个连接同时进入

import threading
import time
   
num = 0
def run2(n):
    time.sleep(1)  
    global num  
#     lock.acquire()  #锁住，只有一个线程能操作
#     num += 1
#     print '%s' % num
#     lock.release()  #解锁

    samp.acquire()  #锁住，只有一个线程能操作
    num += 1
    print '%s' % num
    samp.release()  #解锁

#lock = threading.Lock()  #创建锁
samp = threading.BoundedSemaphore(4)  #允许同时有4个线程进入
 
for item in range(50): #起200个线程
    t2 = threading.Thread(target=run2,args=(item,)) 
    t2.start()
    
    
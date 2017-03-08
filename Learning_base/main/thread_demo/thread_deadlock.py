#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#线程锁

import threading
import time

num = 0  #全局变量
num2 = 0
  
def run(n):
    time.sleep(1)  
    global num  #函数内不能直接使用全局变量，要用就必须用global指定
    global num2
    lock.acquire() #锁住
    num += 1
    lock.acquire()  #等待上一个锁被解锁后再锁住，因此被阻塞住。这就是死锁
    num2 += 2
    
    lock.release()  #解锁
    lock.release()  #解锁
    print '%s\n' % num
 
#lock = threading.Lock() #创建锁，获取一把锁后，不解锁，再获取一把锁，会成死锁
lock = threading.RLock() #创建递归锁。获取一把锁后，内部计数器+1，再获取一把锁，计数器再+1，不会死锁，但是内部计数器的数字有多少，就要依次释放多少次锁，否则会阻塞住。
      
for item in range(50): #起200个线程，去运行run函数对num变量+1，有可能会发生多个线程抢占num变量的结果，导致数据发生错乱
    t = threading.Thread(target=run,args=(item,)) 
    t.start()


    
    
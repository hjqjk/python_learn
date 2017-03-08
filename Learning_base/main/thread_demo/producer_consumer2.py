#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#生产者和消费者模型，还不是很理解
#最大特点：效率高（异步），解耦合

import threading
import random
import time
import Queue

def Producer(name,queue):
    while True:
        if queue.qsize() < 3:
            queue.put('包子')
            print '%s:make a 包子... ----------' %(name,) 
        else:
            print '有5个包子'
        time.sleep(random.randrange(5)) 
            
def Consumer(name,queue):
    while True:
        try:
            #queue.get() #阻塞等待
            queue.get_nowait()  #不等待
            print '%s:get a 包子...' % (name,)
        except Exception:
            print '没有包子了'
        time.sleep(random.randrange(3))

q = Queue.Queue()  #创建队列

p1 = threading.Thread(target=Producer,args=('hjq',q))
p2 = threading.Thread(target=Producer,args=('jk',q))
p1.start()
p2.start()

c1 = threading.Thread(target=Consumer,args=('CC',q))
c2 = threading.Thread(target=Consumer,args=('DD',q))
c1.start()
c2.start()





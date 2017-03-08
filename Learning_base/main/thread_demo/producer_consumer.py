#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from threading import Thread
from Queue import Queue
import time

'''
队列：
    先进先出
    线程安全
'''

class Procuder(Thread): #生产者
    def __init__(self,name,queue):
        '''
        @param name:生产者的名称
        @param queue:容器 ,队列
        '''
        self.__name = name
        self.__Queue = queue
        super(Procuder,self).__init__()  #调用父类的初始化函数,新式类的写法
    
    def run(self):
        while True:
            if self.__Queue.full(): #队列满了，则休息1秒
                time.sleep(1)
            else:
                self.__Queue.put('包子')
                print '%s 生成了一个包子' % (self.__name,)
                time.sleep(1)
        
class Consumer(Thread):  #消费者
    def __init__(self,name,queue):
        '''
        @param name:消费者的名称
        @param queue:容器，队列  
        '''
        self.__name = name
        self.__Queue = queue
        super(Consumer,self).__init__()  #调用父类的初始化函数

    def run(self):
        while True:
            if self.__Queue.empty(): #容器里有东西就拿，没有则休息1秒
                time.sleep(1)
            else:
                self.__Queue.get()
                print '%s 消费了一个包子' % (self.__name,)
                time.sleep(1)    
        
queue = Queue(maxsize=100)  #创建一个队列，长度为100

#三个生产者
procuder1 = Procuder('jk',queue)
procuder1.start()
procuder2 = Procuder('hjq',queue)
procuder2.start()
procuder3 = Procuder('hjqjk',queue)
procuder3.start()

#20个消费者
for item in range(20):
    name = 'consumer%d' %(item,)
    temp = Consumer(name,queue)
    temp.start()


#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import threading
import time

#异步
#不是很理解

def producer(): 
    print '厨师：等人来买'
    event.wait()  #等待
    event.clear()  #清空set
    
    print '厨师：顾客来了'
    print '厨师：开始做包子了'
    time.sleep(3)
    
    print '厨师：你的包子好了'
    event.set()

def consumer():
    print '顾客：饿了，去买包子'
    event.set()  #事件确认
    
    time.sleep(2)
    print '顾客:等待包子制作完成'
    while True:
        if event.isSet(): #判断等待包子是否做好了
            print '谢谢厨师做的包子，真好吃'
            break
        else:  #没收到厨师的信息时，就做自己的事
            print '还没好吗？'
            time.sleep(1)
    
    
event = threading.Event() #创建event对象

p1 = threading.Thread(target=producer)
c1 = threading.Thread(target=consumer)

p1.start()
c1.start()



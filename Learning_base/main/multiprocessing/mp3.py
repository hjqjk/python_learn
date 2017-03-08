#!/usr/bin/env python
#_*_ coding:utf-8 _*_


from multiprocessing import Process,Value,Array
#Value：被封装后的数值类型
#Array：被封装的列表

def f(n,a,raw):
    n.value = 3.1415
    for i in range(5):  
        a[i] = -a[i]  #在子进程中，修改列表数据。如果进程不共享，子进程中修改的数据不会影响到父进程的数据
    raw.append(999)  #如果进程间内存共享了，raw列表会多出元素：999
    print '子进程：',raw
    
if __name__ == '__main__':
    num = Value('d',0.0)  #利用Value建值，进程间内存可共享
    arr = Array('i', range(10)) #利用Array建列表，进程间内存可共享
    print num.value
    print arr[:]
    
    raw_list = range(10)  #原生列表

    p = Process(target=f,args=(num,arr,raw_list))  #起一个子进程，克隆一份主进程的数据，传入几个值
    p.start()
    p.join()
    
    print num.value  #值被改变，进程间内存数据被共享
    print arr[:]   #值被改变，进程间内存数据被共享
    print raw_list  #并没发现元素999，说明这样操作，进程间内存数据是不共享的
    

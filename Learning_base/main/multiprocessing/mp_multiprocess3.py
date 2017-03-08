#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#利用Pool的map，起多进程
from multiprocessing import Pool
import time

def f(x):
    time.sleep(0.5)
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=5)
    res_list = []
    
    for i in range(10):  #处理
        res = pool.apply_async(f,[i,])  #新建一个进程，异步：只是启动进程，不用等待该进程处理完成，可以继续创建新进程
        #相当于：res = Process(target=f,args=[i,])
        
        #res = pool.apply(f,[i,]) #同步：启动一个进程，必须等待该进程处理完成了，才能继续启动新进程
        
        print '---:',i
        print type(res)
        #print res.get()  #在此处用get()，会阻塞，是串行处理：新建一个进程，等待获取值，再新建一个进程，等待获取值，循环...
        res_list.append(res)  #将进程对象存入列表中,并行处理，不会阻塞
    
    for r in res_list: #显示值
        print r.get()
        
        
        
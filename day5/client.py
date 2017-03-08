#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import socket
import os

def chat(): #聊天
    ip_port = ('127.0.0.1',9292)
    client = socket.socket()
    client.connect(ip_port)  #连接server
    
    while True:
        data = client.recv(1024) #接收server发来的数据
        print 'server:'+data
        send_mesg = raw_input('client:')
        client.send(send_mesg)
        if send_mesg == 'exit':  #输入'exit'则退出
            break
    client.close()
    
def upload(): #上传文件
    ip_port = ('127.0.0.1',9191)
    client = socket.socket()  #实例化socket对象
    client.connect(ip_port) #与server端建立连接
    
    data = client.recv(1024) #接收server端传来的消息
    print data
    
    while True:
        inputstr = raw_input('path:')
        if inputstr == 'exit': #输入'exit'则退出
            break
        cmd,path = inputstr.split('|')
        file_name = os.path.basename(path)  #获取文件名
        file_size = os.stat(path).st_size #获取文件的大小
        
        client.send(cmd+'|'+file_name+'|'+str(file_size))  #发送消息（注意格式）：命令|文件名|文件大小
        
        send_size = 0
        f = open(path,'rb')
        Flag = True
        while Flag:
            if  (send_size + 1024) > file_size: #当发送的最后一段 小于 1024 字节
                data = f.read(file_size - send_size) #计算剩余的字节（小于1024），并发送
                Flag = False
            else:
                data = f.read(1024) #每次发送1024个字节
                send_size += 1024  #记录发送大小
            client.send(data)  #向server端发送消息
            
        f.close()  #关闭文件
    client.close() #关闭连接
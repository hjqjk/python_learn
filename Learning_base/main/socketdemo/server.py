#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import socket

ip_port = ('127.0.0.1',9999)

sk = socket.socket()  #实例化socket对象
sk.bind(ip_port)  #将服务绑定在ip和端口上进行监听
sk.listen(5)    #最多可同时处理5个请求，第6个再来就会被阻塞

while True:
    conn,address = sk.accept() #接收请求
    conn.send('welcome..')  #响应请求
    flag = True
    while flag:  #持续接收client发来的消息
        data = conn.recv(1024) #接收client传来的消息，定义最多可接收1024字节
        print data
        if data == 'exit':
            flag = False 
        conn.send('sb')  
    conn.close()  #关闭这次连接
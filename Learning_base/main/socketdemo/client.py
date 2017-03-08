#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import socket

ip_port = ('127.0.0.1',9999)

sk = socket.socket()  #创建socket对象
sk.connect(ip_port)   #与服务端建立连接

while True:
    data = sk.recv(1024) #接收服务端发来的消息
    print data
    send_mesg = raw_input('client:')
    sk.send(send_mesg)
    if send_mesg == 'exit':
        break
sk.close() #关闭这次连接


#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import paramiko

t = paramiko.Transport(('192.168.1.135',22)) #建立一个加密通道
t.connect(username='root',password='123456') #建立连接

channel = t.open_session() #连接成功后打开一个channel
channel.settimeout(30) #设置回话超时时间
channel.get_pty()  #打开远程的terminal
channel.invoke_shell() #激活terminal

#激活terminal后，就可以通过send和recv来远程执行名和接收反馈信息
channel.send('date')
print channel.recv(65535)

channel.close() 
t.close()




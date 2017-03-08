#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import paramiko

#连接认证，通过用户名和密码
t = paramiko.Transport(('192.168.1.135',22)) #建立一个加密通道
t.connect(username='root',password='123456') #建立连接
 
#复用之前的SSH连接，不需要再次认证
sftp = paramiko.SFTPClient.from_transport(t) #建立一个sftp客户端对象
 
sftp.put('D:/temp/test.txt','/tmp/test.txt')  #把本地文件上传到远程服务器
 
sftp.get('/tmp/test.txt','D:/temp/test2.txt')  #把远程服务器上的文件下载到本地
 
t.close()

#########################################

#连接认证，通过私钥文件
private_key_path = 'c:/Users/hjq/.ssh/id_rsa'  #指定私钥文件路径
key = paramiko.RSAKey.from_private_key_file(private_key_path)  #加载私钥文件

t2 = paramiko.Transport(('192.168.1.135',22)) #建立一个加密通道
t2.connect(username='root',pkey=key) #建立连接,通过私钥文件认证

sftp2 = paramiko.SFTPClient.from_transport(t2)

sftp2.put('D:/temp/nginx_conf.txt','/tmp/nginx_conf.txt')  #把本地文件上传到远程服务器

sftp2.get('/tmp/nginx_conf.txt','D:/temp/nginx_conf2.txt')  #把远程服务器上的文件下载到本地

t2.close()



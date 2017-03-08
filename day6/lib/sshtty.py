#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import paramiko

class Sshtty(object):  #ssh连接
    
    def __init__(self,ip,port,user,password):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        
    def remote_command(self,command):  #执行远程命令
        ssh = paramiko.SSHClient()  #创建对象
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #用于添加客户端的主机key到服务器的known_hosts文件中
        ssh.connect(self.ip,self.port,self.user,self.password)  #连接
        
        stdin,stdout,stderr = ssh.exec_command(command)  #远程操作命令，接收结果
        print '--- %s ------' % (self.ip,)
        print stdout.read()   #打印执行结果
        
        ssh.close() #关闭连接
        
    def upload(self,local_path,remote_path):  #上传文件
        t = paramiko.Transport((self.ip,self.port))  #建立加密通道
        t.connect(username=self.user,password=self.password)  #建立连接
        
        sftp = paramiko.SFTPClient.from_transport(t)  #基于上面的连接，建立一个sftp客户端对象
        sftp.put(local_path,remote_path)  #上传文件到远程服务器
        print '--- %s ------' % (self.ip,)
        print '--- 上传成功~' 
        
        t.close()
        
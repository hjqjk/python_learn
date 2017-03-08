#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#利用paramiko模块，连接远程服务器
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #用于添加客户端的主机key到服务器的known_hosts文件中
ssh.connect('192.168.1.135',22,'root','123456')  #连接
stdin,stdout,stderr = ssh.exec_command('ifconfig')  #命令操作，接收结果
print stdout.read()
ssh.close()
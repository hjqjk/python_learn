#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#利用paramiko模块，连接远程服务器,用私钥文件连
import paramiko

private_key_path = 'c:/Users/hjq/.ssh/id_rsa'  #指定私钥文件路径
key = paramiko.RSAKey.from_private_key_file(private_key_path)  #加载私钥文件

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #用于添加客户端的主机key到服务器的known_hosts文件中
ssh.connect('192.168.1.135',22,'root',pkey=key)
stdin,stdout,stderr = ssh.exec_command('ifconfig')
print stdout.read() #打印远程命令的执行结果
ssh.close()  #关闭连接
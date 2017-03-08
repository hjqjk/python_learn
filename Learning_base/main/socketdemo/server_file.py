#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import SocketServer #异步多线程
import os

class MyServer(SocketServer.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        base_path = 'D:/temp/'   #上传目录
        conn = self.request  #client的连接
        conn.send('connected...')
        while True:
            pre_data = conn.recv(1024)  #接收client传来的消息
            cmd,file_name,file_size = pre_data.split('|')  #分割字符串，获取请求方法、文件名、文件大小 
            file_path = os.path.join(base_path,file_name)           
            recv_size = 0  #已经接收的大小
            f = open(file_path,'wb') #打开文件句柄
            Flag = True
            while Flag:  
                if int(file_size) > recv_size:  #没接收完整前，一直循环接收
                    data = conn.recv(1024) #最多接收1024个字节，有可能少于1024字节
                    recv_size += len(data)
                else:   #接收完成
                    recv_size = 0 #已经接收的大小归0，等待下一次接收
                    Flag = False
                f.write(data)  #每次接收到写到文件中
            print 'upload successed.'
            f.close()  
            
    def finish(self):
        pass
    
if __name__ == '__main__':
    ip_port = ('127.0.0.1',8888)
    server = SocketServer.ThreadingTCPServer(ip_port,MyServer)   #实例化异步多线程的socket对象
    server.serve_forever()  #处理
#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#异步多线程
#同时处理多个client请求
import SocketServer
import os

class MyServerFile(SocketServer.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self): #处理请求
        base_path = 'D:/devpy/day5/files/'   #上传目录
        conn = self.request  #client的连接
        conn.send('connected...')
        while True:
            pre_data = conn.recv(1024)  #接收client传来的消息
            if pre_data == 'exit':
                break
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
            conn.send('upload successed...')  #上传成功，给client发消息
            f.close()  

    def finish(self):
        pass

if __name__ == '__main__':
    
    #启动sever服务，用于上传下载
    serverfile = SocketServer.ThreadingTCPServer(('127.0.0.1',9191),MyServerFile)
    serverfile.serve_forever()     
    
    
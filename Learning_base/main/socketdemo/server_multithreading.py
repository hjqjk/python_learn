#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#异步多线程
#能同时处理多个客户端的连接
import SocketServer

class MyServer(SocketServer.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        self.request.send('welcome..')  #响应请求
        flag = True
        while flag:  #持续接收client发来的消息
            data = self.request.recv(1024) #接收client传来的消息，定义最多可接收1024字节
            print data
            if data == 'exit':
                flag = False 
            self.request.send('Yeah~~') #server端发送消息给client端

    def finish(self):
        pass

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    server.serve_forever()
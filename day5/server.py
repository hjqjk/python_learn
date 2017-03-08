#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#异步多线程
#同时处理多个client请求
import SocketServer
from conf import chat_mesg
from lib.common import get_uid
from model import chat_records

class MyServer(SocketServer.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self): #处理请求
        uid = get_uid('./files/uid.pickle')  #获取已经登录的uid
        self.request.send('欢迎 ~~~')  #响应请求
        chat_records.insert_mesg(uid,'server','欢迎 ~~~')  #聊天记录写到数据库里
        while True:
            data = self.request.recv(1024)  #接收client发来的信息，一次最多能接收1024字节
            if data == 'exit': #当收到client传来的'exit'时，跳出循环，server端也不再接收client的消息
                break
            chat_records.insert_mesg(uid,'client',data) #聊天记录写到数据库里
            matching_keyword = check_keyword(data, chat_mesg.keys()) #匹配关键字
            if matching_keyword:  #关键字匹配上
                self.request.send(chat_mesg[matching_keyword]) #发给client
                chat_records.insert_mesg(uid,'server',chat_mesg[matching_keyword]) #聊天记录写到数据库里
            else:
                msg = '这个我还不太懂，咱们聊点别的吧!'
                self.request.send(msg)  #发给client
                chat_records.insert_mesg(uid,'server',msg) #聊天记录写到数据库里
        self.request.close()

    def finish(self):
        pass
    
def check_keyword(mesg,keyword_list): #匹配关键字
    for keyword in keyword_list:
        if mesg.__contains__(keyword):  #匹配关键字，匹配上则返回该关键字
            return keyword
            break

if __name__ == '__main__':
    #启动server服务,用于聊天
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9292),MyServer)
    server.serve_forever()     

    
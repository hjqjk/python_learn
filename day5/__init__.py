#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import SocketServer
import sys
import client
from model.admin import check_login
from lib.common import show_menu
from lib.common import get_uid
from model.chat_records import select_mesg

if __name__ == '__main__': 
    if check_login(): #登录成功才能聊天
        while True:
            choice = show_menu()  #显示菜单并选择
            if choice == 1:  #聊天
                client.chat()  #启动client，聊天
            elif choice == 2:  #查看聊天信息
                uid = get_uid('./files/uid.pickle')
                mesg_tuple = select_mesg(uid)  #查询该uid的聊天记录
                for mesg in mesg_tuple:
                    print mesg['speaker']+':'+mesg['chat_text']
            elif choice == 3:  #上传文件
                client.upload() #上传
            else:
                sys.exit('退出系统')
    else:
        sys.exit('密码连续输错了三次，程序退出.')
        

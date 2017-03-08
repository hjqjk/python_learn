#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from models.admin import check_login
import sys
from lib.common import main_menu
from models.groups_host import Groups_host
from lib.common import group_property
from lib.common import hosts_menu
from lib.common import host_operation

if __name__ == '__main__':
    uid = check_login()  #验证用户，并且获取用户uid
    if uid:
        while True:
            choice = main_menu(uid)  #接收选择，返回值为元组
            grouphost = Groups_host(uid)  #创建主机组对象
            groups = grouphost.get_group()  #查询指定uid的主机组信息
            if choice[0] in range(1,len(groups)+1): #选择主机组列表中的组名
                choice_gid = choice[1]
                host_operation(choice_gid) #批量操作主机组里的所有主机，执行命令和分发文件
            elif choice[0] == len(groups)+1: #修改主机组：增加，删除，改名
                group_property(uid)  #修改组
            elif choice[0] == len(groups)+2: #主机：添加，删除
                hosts_menu(uid)
            else:
                sys.exit('退出系统')
    else:
        sys.exit('用户名或密码连续输错三次，程序退出。')
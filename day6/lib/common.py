#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import hashlib
from models.groups_host import Groups_host
from models.hosts import Hosts
from threading import Thread
from lib.sshtty import Sshtty

def md5_password(password): #对密码进行hash计算
    hashmd5 = hashlib.md5()
    hashmd5.update(password)
    return hashmd5.hexdigest() #返回32位的16进制字符串
    
    
def main_menu(uid): #显示登录页面的菜单
    grouphost = Groups_host(uid)  #创建主机组对象
    groups = grouphost.get_group()  #查询指定uid的主机组，返回结果是元组形式
    serial_number = 0  #用做下标，还用作展示主机组列表的序号
    print '-----------------------------------------'
    print "主机组列表："
    while serial_number < len(groups):
        print "\t %s:  %s" % (serial_number+1,groups[serial_number]['gname']) #打印序号和主机组名，下标号+1作为序号
        serial_number += 1 
        
    print "管理操作：\n\t %s:  修改主机组" % (serial_number + 1,)
    serial_number += 1
    print "\t %s:  添加/删除主机" % (serial_number + 1,)
    serial_number += 1
    print "\t %s:  退出系统" % (serial_number + 1,)
    
    while True: #选择操作，并且返回
        operation = input("请选择操作(1/2/3/4...)：")
        if operation in range(1,len(groups)+4):
            if operation <= len(groups): 
                return (operation,groups[operation-1]['gid'])  #获取选择序号和对应的gid
            else:
                return (operation,'')
            break
        else:
            print "--- 输入错误，请重新输入。"
            
def group_property(uid):  #增加新组，删除组，修改组名
    print '-----------------------------------------'
    print "1、增加新组"
    print "2、删除组"
    print "3、修改组名"
    
    grouphost = Groups_host(uid)
    choice = raw_input("请选择操作(1/2/3)：")
    if choice == '1':  #添加新组
        while True:
            gname = raw_input("输入新的组名：")
            if not grouphost.select_group(gname):  #组名不存在，则添加新的组名
                grouphost.add_group(gname)  #添加新的组名
                print '--- 添加新组成功~'
                break
            else:
                print '--- 组名：%s，已经存在.请重新输入~' % (gname,)
    elif choice == '2':  #删除组
        gname = raw_input("输入要删除的组名：")
        if grouphost.del_group(gname):  #删除指定的组
            print '%s组删除成功' % (gname,)
        else:
            print '--- 没有这个组名：%s' % (gname)
    elif choice == '3':  #修改组名
        while True: 
            gname = raw_input("要修改的组名：")
            if grouphost.select_group(gname):   
                gnew_name = raw_input("新的组名：")
                break
            else:  #要修改的组名不存在，则不能修改
                print '--- 组名：%s 不存在，请重新输入~' % (gname,)       
        grouphost.rename_group(gname, gnew_name)  #修改组名
        print '--- 组名修改成功~'
    else:
        print "--- 输入错误，请重新操作"

def hosts_menu(uid):   #主机操作菜单，增加/删除主机
    print '-----------------------------------------'
    print '1、增加新的主机'
    print '2、删除主机'
    
    hosts = Hosts()
    grouphost = Groups_host(uid)
    
    choice = raw_input("请选择操作(1/2)：")
    if choice == '1':   #增加主机
        while True:
            gname = raw_input("选择加入的主机组：")
            group = grouphost.select_group(gname)
            if group: #判断是否有这个组
                gid = group[0]['gid']  #取得主机组id：gid
                break
            else:  
                print '--- 没有这个组：%s，请重新输入。' % (gname,)
        ip = raw_input("IP地址:")    #录入ip，端口，用户，密码
        port = raw_input("端口：")
        user = raw_input("用户名：")
        password = raw_input("用户密码：")
        
        hosts.add_host(ip, port, user, password, gid)  #添加主机
        print '--- 主机添加成功~'
    else:    #删除主机
        while True:
            gname = raw_input("选择删除哪个主机组里的主机：")
            group = grouphost.select_group(gname)
            if group:
                gid = group[0]['gid']
                hosts_list = hosts.select_group_host(gid)  #查询指定组的主机列表
                print '主机组：%s 的主机列表：'  % (gname,)  
                for host in hosts_list: #打印该主机组的主机列表
                    print host['ip']
                host_ip = raw_input("输入要删除的主机ip：")
                hosts.del_host(host_ip, gid)  #删除主机
                print '--- 主机删除成功~'
                break
            else:
                print '--- 没有这个组：%s，请重新输入。' % (gname,)

def host_operation(gid):   #选择主机组后的操作
    print '-----------------------------------------'
    print '1、批量执行远程命令'
    print '2、批量推送文件'
    
    hosts = Hosts()
    hostsmesg = hosts.get_all(gid)  #查询该组的主机列表
    
    choice = raw_input("请选择操作(1/2)：")
    if choice == '1':  #批量执行远程命令
        command = raw_input('请输入命令：')
        for host in hostsmesg:
            sshtty = Sshtty(host['ip'],host['port'],host['user'],host['password'])
            t = Thread(target=sshtty.remote_command,args=(command,))  #创建线程，多个主机就起多个线程处理
            t.start()
            t.join(2)  #先执行2秒钟子线程的操作。2秒过后，执行主线程操作。
    elif choice == '2':  #批量推送文件
        local_path = raw_input("输入本地文件路径：")
        remote_path = raw_input("输入远程文件路径：")
        for host in hostsmesg:
            sshtty = Sshtty(host['ip'],host['port'],host['user'],host['password'])
            t = Thread(target=sshtty.upload,args=(local_path,remote_path))
            t.start()
            t.join(2)  #先执行2秒钟子线程的操作。2秒过后，执行主线程操作。
    else:
        print '输入错误，请重新选择'
    
    

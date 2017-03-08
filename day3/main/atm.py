#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import sys
import pickle
import time
import hashlib

def md5_password(password): #对密码进行hash，避免以明文方式存储密码
    hashmd5 = hashlib.md5() #生成一个MD5对象
    hashmd5.update(password)
    return hashmd5.hexdigest() #返回32位的16进制字符串

def show_menu(): #显示登录页面的菜单
    print "\t 1:  取现"
    print "\t 2:  查询"
    print "\t 3:  还款"
    print "\t 4:  转账"
    print "\t 5:  退出"
    while True:
        operation = input("请选择操作(1/2/3/4/5)：")
        if operation in [1,2,3,4,5]:
            return operation
            break
        else:
            print "输入错误，请重新输入。"
            
def log(card_number,digest,cash,handing_charge,target): #记录交易日志
    f = open('../db/user_deal.log','a+')
    log_list = [str(card_number)+'\t',str(time.time())+'\t',digest+'\t',str(cash)+'\t',str(handing_charge)+'\t',str(target)+'\n'] #转为字符串，再与'\t'连接
    f.writelines(log_list) #写到日志文件中，每次写一行
    f.close()

def auth(account,card_number,card_password): 
    error_count = 0 #输错密码的次数
    # 用户认证环节，分四种情况：用户不存在，用户被锁了，用户存在密码输错，用户密码都输对
    while account.has_key(card_number):  #用户存在
        if account[card_number]['locked'] == 1:  #用户被锁
            print "卡号 :%s 已经被锁了，请先去柜台解锁" % card_number
            return 0  #不成功状态
            break  #退出
        elif account[card_number]['password'] == md5_password(card_password): #用户和密码都正确
            print '欢迎登录本系统 ~~~'
            return 1  #成功状态
            break
        else:
            if error_count == 2:  # 如果密码输错三次，则锁住该用户
                print "你的卡号:%s，因输错三次密码被锁！" % card_number
                account[card_number]['locked'] = 1  
                return 0 #不成功状态
                break
            else:
                print '你的密码输错了，请再次输入!'
                card_password = raw_input("你的卡号密码：")     
                error_count += 1   
    else:  #用户不存在
        print '卡号:%s 不存在，请确认该卡的有效性!' % card_number
        return 0  #不成功状态

def fast_cash(account,card_number): #提现功能
    while True:
        cash = input("输入你要取的金额:") 
        if cash*1.05 > account[card_number]['balance']: #余额不足
            print '余额不足，不能取'
            break
        elif cash%100 != 0: #需要整百地取现
            print "输入错误，只能整百取"
            continue
        else:
            account[card_number]['balance'] -= cash*1.05  #取现，扣除%5手续费
            flush(account,'../db/account.db') #实时刷新到文件中
            print "你成功取现 %d元，手续费是%d元，账号余额为%d元 " % (cash,cash*0.05,account[card_number]['balance'])
            log(card_number, '取现', cash, cash*0.05, card_number) #记录交易明细
            break

def query(account,card_number): #查询余额和交易明细
    print "你的账号余额是：%s 元" % account[card_number]['balance']
    f = open('../db/user_deal.log','r')
    for line in f.xreadlines():
        loglist = line.split()
        if loglist[0] == card_number:
            struct_time = time.localtime(float(loglist[1])) #时间戳 转 元组形式
            str_time = time.strftime("%Y-%m-%d %H:%M:%S",struct_time) #元组形式 转 字符串形式
            print "用户:%s，交易时间:%s，交易类型:%s，交易金额:%s元，手续费:%s元，对象:%s" %(loglist[0],str_time,loglist[2],loglist[3],loglist[4],loglist[5])
    f.close()    

def repayment(account,card_number): #还款或存钱
    while True:
        cash = input("还款金额：")
        if cash > 0 :
            account[card_number]['balance'] += cash #将还款金额加到余额上
            flush(account,'../db/account.db') #实时刷新到文件中
            print "你成功还款 %d元，手续费是%d元，账户余额为%d元" % (cash,cash*0,account[card_number]['balance'])
            log(card_number, '还款', cash, cash*0, card_number) #记录还款日志
            break
        else:
            print "金额输入错误，请重新输入。"   

def transfer_accounts(account,card_number): #转账
    target = raw_input("收款账户：")
    cash = input("转账金额：")
    if target in account: #判断收款账户是否存在
        if cash <= account[card_number]['balance']:
            account[card_number]['balance'] -= cash  #扣除转账金额
            account[target]['balance'] += cash  #收款账户增加金额
            flush(account,'../db/account.db') #实时刷新到文件中
            print "你成功转账%d元,收款人是%s，手续费是%d元，账户余额是%d元，" %(cash,target,cash*0,account[card_number]['balance'])
            log(card_number, '转账', cash, cash*0, target) #记录交易日志。转账手续费为0元
        else:
            print "余额不足，不能转账"
    else:
        print "收款账户并不存在"
    
def logout(): #退出
    print '系统退出~'
    flush(account,'../db/account.db')  #退出系统前，必须先将修改的数据刷新到文件中
    sys.exit()
    
def flush(account,fo): #将修改过的数据，序列化到文件中
    f2 = open(fo, 'w')           
    pickle.dump(account,f2) 
    f2.close()

if __name__ == '__main__':
    card_number = raw_input("你的卡号：")
    card_password = raw_input("你的卡号密码：")
    
    f = open('../db/account.db', 'r')  
    account = pickle.load(f)  #加载序列化文件的数据到内存
    f.close()
    
    login_sucess = auth(account,card_number, card_password)  #验证用户和密码
    while True:
        if login_sucess == 1:
            operation = show_menu()  #显示主页操作选项
            if operation == 1:
                fast_cash(account,card_number) #取现
            elif operation == 2:
                query(account,card_number) #查询
            elif operation == 3:
                repayment(account,card_number) #还款
            elif operation == 4:
                transfer_accounts(account,card_number) #转账
            else:
                logout() #退出
        else: 
            logout()

    flush(account,'../db/account.db') #将内存中修改的数据，刷新到文件中

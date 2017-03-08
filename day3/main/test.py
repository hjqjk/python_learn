#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#!/usr/bin/env python
#coding=utf-8
# Name: AtmCard.py
 
__author__ = 'kumikoda'
 
import pickle
import sys
import time
import hashlib
import os
 
def main():
    '''打印功能信息列表,并提供用户输入接口再进行具体项目操作'''
    cardNum = login('id')
    if cardNum == False:
        sys.exit()
    while True:
        wecome = raw_input("""欢迎使用本银行信用卡中心! 请输入如下功能对应的数字.
                    功能如下:
                    1. 第一次使用卡,请对卡进行初始化操作(重要).
                    2. AMT现金取款
                    3. 购物、消费等刷卡消费
                    4. 信用卡还款
                    5. 退出
        Please input(1/2/3/4/5):""").split()
        if len(wecome) == 0:
            continue
        number = wecome[0]
        if number == '1':
            init()
            continue
        elif number == '2':
            draw_money(cardNum)
        elif number == '3':
            buy(cardNum)
        elif number == '4':
            repayment(cardNum)
        elif number == '5':
            print "Exit, Good Bye!"
            sys.exit()
        else:
            print "你输入的数字不在功能列表内,请重新输入."
            continue
 
def login(number=None):
    '''用户登录验证'''
    with open('../db/Balance_tab','rb') as f:  # 读取文件并将数据放入元组
        for line in f:
            keys = line.split()[1]
            print keys
            vlues = line.split()[2]
            print vlues
            con = 0
            while True:
                CardNum = raw_input("\033[32;1m请输入您的信用卡卡号:")
                if CardNum == keys:
                    UserPwd = raw_input("\033[32;1m请输入你的登录密码:")
                    md5 = hashlib.md5()
                    md5.update(UserPwd)
                    UserPwd = md5.hexdigest()
                    print md5.hexdigest()
                    if UserPwd == vlues:
                        print "登录成功."
                        if number == "id":
                            return CardNum
                        else:
                            return True
                    else:
                        con = con + 1
                        print "输入的密码或者用户名有误,请重新输入,[Error %s]" % con
                        if con == 3:
                            print "输入的密码错误三次."
                            return False
                        else:
                            continue
                else:
                    print "没有找到你输入的卡号,请重新输入."
                    continue
 
def init():
    '''新卡初始化(1.额度加载 2.设置修改卡密码 3. 添加记账日志格式头部)'''
    money = []
    with open('../db/Balance_tab','rb') as f:
        m = f.read().split()[-1]
        money.append(m)
        temp_log(Tlist=money, content='dump')
        print "Temp money load OK."
    initDlist = ['账号' + '时间' + '\t', '摘要' + '\t', '消费金额' + '\t', '手续费' + '\n']
    day_log(initDlist)
    print "Day log write OK."
 
def draw_money(cardNum):
    '''取现功能'''
    while True:
        input_money = raw_input("欢迎使用本中心自助取款ATM系统,请输入本次取款金额:")
        if len(input_money.split()) == 0:
            continue
        userinfo = raw_input("取现需收取%5的手续费,确认是否取现[Y/n]:")
        if userinfo == "Y" or userinfo == "y":
            ## load总金额,并计算输出
            t1 = temp_log(content='load')
            money = float(t1[0])
            fee = float(input_money) * 0.05  # 手续费
            draw = float(input_money) + fee  # 本次取款额+手续费
            if draw >= money:
                print "账户余额不足,请重新输入取款金额."
                continue
            else:
                total = money - draw      # 账户余额 - 本次取款额
                print "您本次取现金额为: RMB% s 账户可取现总金额为: RMB% s" %(input_money, total)
                ## dump 消费后总金额,到文件内保存
                totals = []
                totals.append(total)
                temp_log(Tlist=totals, content='dump')
                ## 写入日志文件
                drawtime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())  # 获取当前日期
                Dlist = [cardNum + '\t', drawtime + '\t', 'draw money' + '\t', '-' + input_money + '\t', '-' + str(fee) + '\n']
                day_log(Dlist)
                scont = raw_input("您是否继续取现:[Y/n]")
                if scont == "Y" or scont == "y":
                    continue
                elif scont == "N" or scont == "n":
                    print "Exit!"
                    break
        elif userinfo == "N" or userinfo == "n":
            print "Exit!"
            sys.exit()
        else:
            print "你输入[Y/n]按回车键确认:"
            continue
 
def buy(cardId):
    '''购物/消费等'''
    user_Money = int(temp_log(content='load')[0])
    while True:
        list = {1: ['Iphone 6s', '5000'], 2: ['MacBook', '15000'], 3: ['Tea', '550'], 4: ['Vegetables', '450'], 5: ['coffee', '250']}
        print "购物清单:"
        for x, y in list.items():
            z = ' '.join(y)
            print x, z
        yn_list = raw_input("Do you need to buy [Y/n] or add shoping list [S] Enter:")
        if yn_list == "Y" or yn_list == "y":
            user_input = raw_input("请输入你要购买的商品名称对应的编号:")
            k = int(user_input)
            if len(user_input) == 0:
                print "你没有输入任何商品的名称,请重新输入." 
                continue
            amount = int(list[k][1])   # 取字典中key对应的商品价格
            if user_Money > amount:
                user_Money = user_Money - amount
                print "You need to pay RMB%s totally." % amount
                print "你的账户余额为: RMB%s" % user_Money
                ## 消费写入日志文件
                drawtime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
                defname = sys._getframe().f_code.co_name
                Dlist = [cardId + '\t', drawtime + '\t', defname + ':' + list[k][0] + '\t', '-' + str(amount) + '\t', '0' + '\n']
                day_log(Dlist)
                ## 将消费后金额写入temp文件
                tmp_Money = []
                tmp_Money.append(user_Money)
                temp_log(Tlist=tmp_Money, content='dump')
            elif user_Money < amount:
                print "你的账户余额为: RMB%s" % user_Money
                print "你的账户余额不足已支付本次购物,你可以尝试选择其他商品!"
                continue
            if (user_Money < 100) and (user_Money > 0):
                    print "由于你的账户余额已低于购物清单任何物品单价,系统自动退出购物,请充值后再来购买."
                    sys.exit()
        elif yn_list == "N" or yn_list == "n":
            print "You input %s, exit buy!" % yn_list
            #sys.exit()
            break
        elif yn_list == "S" or yn_list == "s":
            while True:
                shop_id = raw_input("请输入ID号,注意ID号不能重复:")
                shop_m = raw_input("请输入商品名称和价格,中间已单个空格.")
                list[shop_id] = shop_m
                print "成功添加商品到货架."
                print list
                s_input = raw_input("是否继续添加[Y/n]:")
                if s_input == "Y" or s_input == "y":
                    continue
                else:
                    print "Exit, 退出商品添加."
                    break
        else:
            print "You input Other string, please again!"
            continue
 
def day_log(Dlist):
    '''日记账、每月账单导出功能'''
    with open("log.txt", 'a') as df:
        df.writelines(Dlist)
 
def temp_log(Tlist=None, content="load"):
    '''总金额临时记录文件'''
    try:
        if content == "load":
            loadput = open('temp.txt', 'r')
            loaddata = pickle.load(loadput)
            loadput.close()
            return loaddata
        elif content == "dump":
            output = open('temp.txt', 'wb')
            pickle.dump(Tlist, output, protocol=2)
            output.close()
        elif content == "loads":
            data = pickle.loads(Tlist)
            return data
        else:
            print "参数错误,重新输入."
    except Exception, e:
        print e
 
def repayment(cardID):
    '''信用卡还款接口'''
    try:
        while True:
            # 获取初始额度
            with open('../db/Balance_tab','rb') as f:
                s = int(f.read().split()[-1])
            # 截止还款日获取卡内余额
            balance = temp_log(content='load')[0]
            repay = s - balance
            if repay == 0:
                print "您本月已还款,无需还款."
                print "Exit, repayment."
                break
            else:
                print "您本月需要还款金额为: ￥%s" % repay
                h_input = raw_input("确认是否还款,请输入[Y/n]:")
                if h_input == "Y" or h_input == "y":
                    amount_in = raw_input("请输入您本次还款金额:")
                    if float(amount_in) > repay:
                        print "您输入的还款额超过本月消费金额,请重新输入."
                        continue
                    else:
                        dumppay = float(amount_in) + balance
                        # dump到temp文件
                        dpay = [dumppay]
                        temp_log(Tlist=dpay, content='dump')
                        print "还款成功."
                        # 记录到流水日志
                        paytime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
                        repadyLog = [cardID + '\t', paytime + '\t', "repayment" + '\t', '+' + amount_in + '\t', '0' + '\n']
                        day_log(repadyLog)
                elif h_input == "N" or h_input == "n":
                    print "Exit, repayment system."
                    break
                else:
                    print "Please input again."
                    continue
    except Exception, e:
        print e
 
if __name__ == '__main__':
        main()
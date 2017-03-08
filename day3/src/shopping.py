#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import pickle
from atm import md5_password
from atm import flush
from atm import log

def auth_charge(total_money): #结算时的卡号和密码认证
    print "欢迎进入结算中心~"
    f = open('../db/account.db', 'r')  
    account = pickle.load(f)  #加载序列化文件的数据到内存
    f.close()
    while True:
        card_number = raw_input("你的卡号：")
        card_password = raw_input("你的卡号密码：")
        if account.has_key(card_number) :  #用户存在
            if account[card_number]['password'] == md5_password(card_password): #用户和密码都正确
                if total_money <= account[card_number]['balance']:
                    account[card_number]['balance'] -= total_money  #扣款
                    flush(account,'../db/account.db') #刷新数据到文件中
                    log(card_number, '购物扣款', total_money, total_money*0, card_number) #记录交易明细
                    print "成功扣款"
                    break
                else:
                    print "账号余额不足，扣款失败"
                    break
            else:
                print "卡号或密码错误，请重新输入"
        else:  #用户不存在
            print '卡号:%s 不存在，请确认该卡的有效性!' % card_number


def shopping(goods): #购物
    shopping_cart = []  #购物车列表
    total_money = 0 #购物商品的总金额
    while True:
        buyNo = input("选购商品(1/2/3...):")
        if (buyNo-1) in range(len(goods)): #判断是否有这个商品
            total_money += goods[buyNo-1]['price']   #统计购买的总金额
            shopping_cart.append(goods[buyNo-1]['name'])  #购买的商品名添加到购物车列表
            select = raw_input("是否要继续购买(y/n): ")
            if select == 'y':
                continue
            else: 
                break
        else:
            print "输入有误，请重新输入：" 
    
    auth_charge(total_money)  #扣款
     
def goods_list(goods):#打印商品列表
    i = 0 #为每个商品标序号
    print "商品列表如下："
    for goods_list in goods: #循环读取商品信息
        i += 1
        print "%d.\t商品名:%s\t单价(元):%d\t库存量(个):%d" % (i,goods_list['name'],goods_list['price'],goods_list['inventory'])    
 
if __name__ == '__main__':
    print "欢迎使用本购物系统~"
    f = open('../db/goods.db','r')
    goods = pickle.load(f) #加载序列化文件的数据到内存
    goods_list(goods)  #打印商品列表
    shopping(goods)
    f.close()
    
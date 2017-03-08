#_*_ coding:utf-8 _*_

# 购物车程序
# 要求用户输入工资，然后打印购物菜单
# 用户可以不断的购买商品，直到钱不够为止
# 退出时格式化打印用户已购买的商品和剩余金额

def listgoods(goods): #列出购买的商品
    for i in range(len(goods)):
        print goods[i]

def init_menu(price,menu): #商品列表，商品单价表初始化，商品菜单表初始化
    for line in f1.readlines():
        print line,  #第一次打印购物菜单
        line = line.strip('\n').split() #读取菜单文件，经split()返回是个列表
        price.append(int(line[1])) #商品单价列表
        menu.extend(line) #将每样商品及其单价存到同一个列表中

if __name__ == '__main__':
    f1 = file('menu.txt','rb')   #menu.txt中存有商品和对应的单价表
    menu = []  #商品名和单价的列表
    price = [] #商品单价列表
    goods = []  #购买的商品表
    
    salary = input("请输入你的工资(元)：")
    print "购物清单，商品及其单价如下："
    init_menu(price,menu)  #打印清单并初始化price和menu列表
    blance = salary  #余额变量

    while blance >= min(price): #如果余额大于等于菜单中商品的最低单价，就可以继续购物
        shop = raw_input("请选择购买的商品: ")
        if shop in menu: #输入的商品名要存在
            index = menu.index(shop)  #获取购买商品名的下标位置
            if blance < int(menu[index+1]): #余额不足
                print "当前余额是：%s。余额不足，不能购买该商品" % blance
                for j in range(0,len(menu),2): #打印商品菜单
                    print menu[j],menu[j+1]       
            else:
                blance -= int(menu[index+1]) #购物后，余额扣除
                goods.append(shop)  #添加商品到购物列表
        else:
            print "没有这个商品，请重新选择~"
    else:
        print "你的余额不足以购买任何一件商品，请充值~~"
    
    print "购买的商品："
    listgoods(goods)
    print "剩余金额：",blance

    f1.close()

# _*_ coding:utf-8 _*_

# 员工信息表查询
# 用户可以模糊查询员工信息
# 显示匹配了多少条，匹配字符需要高亮显示

if __name__ == '__main__':
    mesg = ''
    f1 = file('employee.txt','rb')  #打开员工信息文件
    while True:
        mesg = raw_input('查询：')     
        if mesg == 'q' or mesg == 'quit': #按'q'或'quit'，退出
            break
        else:
            for line in f1.readlines():
                if mesg in line: # 匹配的行
                    linetemp = str(line).replace(mesg,"\033[31m%s\033[0m" % mesg) #匹配字符替换为高亮
                    print linetemp,
        f1.seek(0) #跳回文件开头，以便下一轮查询
    f1.close()

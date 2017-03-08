#!/usr/bin/env python
#_*_ coding:utf-8 _*_

### eval函数 。
# 整个表达式是个字符串，eval函数，能将其直接运算。当读入execl表的数据里，表达式为字符串时，可以使用该函数运算
x = '3*5'
y = '8-3'
z = '2**3'
print eval(x)
print eval(y)
print eval(z)

### compile 和 eval 的结合
com = compile('2**5','', 'eval') #’eval’: 配合eval使用。compile一次编译，多次调用。返回代码对象
print eval(com)

### exec 和 compile 的结合
code = "for i in range(1,6):print i" 
cmpcode = compile(code,'', 'exec') #’exec’: 配合多语句的exec使用
exec(cmpcode)

code2 = "print 'hello world'"
cmpcode2 = compile(code2,'','single') #’single’: 配合单一语句的exec使用
exec(cmpcode2)
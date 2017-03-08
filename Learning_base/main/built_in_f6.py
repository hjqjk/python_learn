#!/usr/bin/env python
#_*_ coding:utf-8 _*_


#反射。
#通过字符串的形式来导入模块，
temp = 'sys'
model = __import__(temp)
print model.path

#并以字符串的形式执行函数
temp2 = 'os'
func = 'getcwd'
model2 = __import__(temp2)
Function = getattr(model2,func)
print Function()

#适应的需求：(适用设计模式中的工厂模式，为了降低代码的耦合性)
#如果有两个不同的数据库sqlserver和mysql模块，都有count函数。
#如今在用：import sqlserver ，所有的代码块里边的函数都是 sqlserver.xxx。
#不幸，sqlserver宕机了，要切换到mysql，去改代码，如何做到快速的一键切换。


### 实现工厂模式
'''
import file.demo
#demo.display()  #报错。这样无法调用display函数
file.demo.display()  #使用file.index.demo才能调用display函数
'''


model_name = 'demo'
func_var = 'log'
model_temp = __import__('file.'+model_name) #导入模块，file.demo
print model_temp
model = getattr(model_temp, model_name)  #必须要用getattr取出demo直接模块对象(仍然没有搞清楚为什么还要用 getattr，__import__不能一步到位吗？)
print model
Func = getattr(model, func_var)
print Func
Func()

## 目前的web框架，根据传入的url的不同调用不同的函数返回相应的结果，底层代码本质用的就是反射


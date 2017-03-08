#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#序列化
import pickle

l1 = ['hjq',26,'xxbb',90]

dumpsed = pickle.dumps(l1)  #序列化，将列表序列化成字符串，内存中
print dumpsed 
print type(dumpsed)

loadsed = pickle.loads(dumpsed) #反序列化，将字符串反序列化成列表，内存中
print loadsed,'\n'


pickle.dump(l1,open('D:/devpy/temp/tmp.pk','w'))  #将列表序列化成字符串并存到文件中
l12 = pickle.load(open('D:/devpy/temp/tmp.pk','r'))  #将文件中的序列化数据 反序列化为列表
print l12


#序列化的用处
#1、用于两个Python程序之间'共享'数据，进程的内存空间是不共享的
#2、比喻：打游戏时，状态都是实时在内存中生成的，可通过每隔一段时间将这些状态序列化保存到文件中，达到存档的效果。
#3、nosql序列化保存数据到文件，用做数据备份。


#pickle 和 json 
#pickle是Python搞得，只能用于Python程序
#json是标准化的数据存储格式，所有语言都支持。不同编程语言间进行内存数据交互时，要选用json
#pickle 能序列化 Python的所有对象，如类、函数、字典、列表、字符串等；json 只能序列化常规的数据类型，如字典、列表、字符串等
#json序列化后的数据，能直观看懂，人可读；pickle序列化后的数据，往往很难看懂，多为无规则的。




#!/usr/bin/env python
#_*_ coding:utf-8 _*_

def test(name,age=10):
    print age,name

def show(**kargs):  #接收字典
    for item in kargs.items():
        print item
        
def show2(*lists): #接收多个参数
    print lists[1]
    for i in lists:
        print i
        
show(name='hjq',age='25')

user_dict = {'k1':123,'k2':234}

show(**user_dict)

l1 = ['hjq','jk','jk123']
dup1 = ('a','b','c')

show2(l1,'bbbb')
show2(dup1,[1,2,3])
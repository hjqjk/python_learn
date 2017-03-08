#!/usr/bin/env python
#_*_ coding:utf-8 _*_

def test(name,age=10): #age参数默认值是10
    print age,name

def show(**kargs):  #接收字典，注意写上**
    for item in kargs.items():
        print item
        
def show2(*lists): #接收多个参数，注意写上*
    print lists[1]  #先打印第二个传参
    for i in lists: #再逐一打印每个传参
        print i
        
test('hjq')  #age参数不传入，则默认为10

show(name='hjq',age='25') #字典的一种传参方式
print '\n'

user_dict = {'k1':123,'k2':234}  #新建一个字典
show(**user_dict)  #注意，一定要加**，否则只是传了一个字典变量，而不是字典的值
#show(user_dict)  #会报错
print '\n'

l1 = ['hjq','jk','jk123']
dup1 = ('a','b','c')

show2(l1,'bbbb')  #传入列表和字符串
print '\n'

show2(dup1,[1,2,3])
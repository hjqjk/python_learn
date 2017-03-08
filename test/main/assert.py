#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#断言：assert，通常用于验证开发期间程序状况的

assert 1==1,'出错时才会显示111' 

print '断言条件为True，继续往下执行'

try:
    assert 1==2,'出错时才会显示222'
    print '断言条件为True'
except AssertionError,e:
    print '断言条件为False，报错：AssertionError'
    print e
    
#assert 1==3,'出错时才会显示333'  #报错
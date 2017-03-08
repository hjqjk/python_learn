#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#异常捕获

try:
    #import xxx
    name = input('输入你的年龄：')
except NameError,e:
    print 1,e
    print '跳转到404页面'
except ImportError,e:  #异常类：ImportError，e代表该异常
    print 2,e
    print '跳转到404页面'
except Exception,e:
    print 3,e
    print '跳转到404页面'
else:  #可选。可加也可以不加else
    print '没有出错时，执行'
finally:  #可选
    print '无论异常与否，都会执行'
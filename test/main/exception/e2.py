#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#自定义异常和手动触发异常

class MyException(Exception):
    def __init__(self,msg):
        self.error = msg
    def __str__(self,*args,**kargs): #一定得是这个函数名:__str__
        return self.error
    
obj = MyException('自定义错误信息')
print obj  #会自动访问__str__函数，返回异常信息

raise MyException('自定义错误信息-----')  #raise手动触发异常
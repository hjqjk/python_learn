#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import hashlib

def md5_password(password): #对密码进行hash计算
    hashmd5 = hashlib.md5() #生成一个md5对象
    hashmd5.update(password)
    return hashmd5.hexdigest()  #返回32位的16进制字符串

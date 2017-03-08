#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import hashlib

hashmd5 = hashlib.md5() #生成一个MD5对象
hashmd5.update('admin') 
passwdmd5 = hashmd5.hexdigest()   #32位的16进制字符串
print passwdmd5
print hashmd5.digest()

hashmd5b = hashlib.md5()
passwd = raw_input('your password:')
hashmd5b.update(passwd)
if hashmd5b.hexdigest() == passwdmd5:
    print 'password is right'
else:
    print 'password is error'
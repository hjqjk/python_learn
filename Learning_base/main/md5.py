#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import hashlib

hashmd5 = hashlib.md5() #生成一个MD5对象
hashmd5.update('admin')  #hash化
passwdmd5 = hashmd5.hexdigest()   #返回32位的16进制字符串
print passwdmd5  
print hashmd5.digest() #返回摘要(16位)，作为二进制数据字符串值
print hashmd5.digest_size  #返回的摘要字节大小

hashmd5b = hashlib.md5()
passwd = raw_input('your password:')
hashmd5b.update(passwd)
if hashmd5b.hexdigest() == passwdmd5:
    print 'password is right'
else:
    print 'password is error'
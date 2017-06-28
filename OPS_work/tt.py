#!/usr/bin/env python
# _*_ coding:utf-8 _*_


f = open('/tmp/t.txt','a+')

s = 'export PROMPT_COMMAND=\'{ msg=$(history 1 | { read x y; echo $y; });logger \"[euid=$(whoami) hostname=$(hostname)]\":$(who am i):[`pwd`]\"$msg\"; }\''

f.write(s)

f.close()


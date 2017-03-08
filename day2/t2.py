#_*_ coding:utf-8 _*_

#开发:文件替换小程序
#使用方法：
#文件名.py  '要替换的内容'  '替换内容' 文件名  
#参数选项：--bak 新文件名   ：自动备份文件
#例子：
#./file_replace.py 'ALEX LI l2' '3714' accounts.txt
#./file_replace.py 'ALEX LI l2' '3714' accounts.txt --bak new_file.txt

import sys,os

if len(sys.argv) < 4: #传参错误，则提示正确用法
    print 'Useage:./t2.py oldtext newtext filename'

#参数被存入sys.argv列表中
oldtext,newtext = sys.argv[1],sys.argv[2]
filename  = sys.argv[3]

oldfile = file(filename,'rb')  #打开文件
newfile = file('.%s.bak' % filename,'wb') #创建一个隐藏的文件

for line in oldfile.readlines():
    newfile.write(line.replace(oldtext,newtext)) #将替换后的字符串写到隐藏文件中，原文件不变

if '--bak' in sys.argv: #如果有--bak参数，则将原文件重命名，隐藏文件重命名为原文件
    os.renames(filename,'%s.bak' % filename)
    os.renames('.%s.bak' % filename,filename)
else:
    os.renames('.%s.bak' % filename,filename)

oldfile.close()
newfile.close()

#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from PIL import Image
import re
from io import BytesIO
import urllib

# 题意：图片中间的灰色带是解题的关键。灰色带的范围：宽：43px到51px ，长：0px到607px
# 求得各位置的像素值（去重），后将像素的（R或G或B）值，装换为ascii码的对应字符

# im = Image.open('files/oxygen.png')
# 另外一种打开图片文件的方法
im = Image.open(BytesIO(urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png").read()))

# 依次获取 x值为(0,607)中，y值固定为 50px 位置的像素值
# 可以看出，x方向，每隔7px的位置，像素值就不一样
# for i in range(0, 607):
#     print im.getpixel((i, 50))

hints = ''
for i in range(0, 607, 7):
    hints += chr(im.getpixel((i,50))[1]) # 获取像素，并选择'G'值将其转换为ascii中的对应字符
print hints  # 出题者给的提示

# print ''.join([chr(im.getpixel((i, 50))[2]) for i in range(0, 607, 7)])

next_level = ''.join([chr(int(i)) for i in re.findall('\d{3}', hints)]) # 根据出题者给的提示，将其中的数字转换为字符

base_url = next_level + '.html'
path_url = "http://www.pythonchallenge.com/pc/def/"

print "\nNext level: "
print "%s%s" % (path_url, base_url)







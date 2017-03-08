#_*_ coding:utf-8 _*_

#print range(10)
#print xrange(10)

#for item in xrange(10):
#    print item
    
    
# 生成器 yield的使用
def HjqxReadline():
    seek = 0
    while True:
        with open('D:/devpy/temp/my.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data  #返回一个生成器对象
            else:
                return
            
print HjqxReadline() #返回一个生成器对象
x = HjqxReadline()
print next(x),
print next(x)

for item in HjqxReadline():
    print item,
#_*_ coding:utf-8 _*

# 列表：['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', 'f', 'a', 'b', 'c', 'e', 'e', 'e', 'd', 'e']
# 查找字符'e'的所有index值

l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', 'f', 'a', 'b', 'c', 'e', 'e', 'e', 'd', 'e']
print l1

s = 'e'
print l1.count(s),'\n'

# 方法一
pos1 = 0  # 从0下标开始
for i in range(l1.count(s)): #l1.count(s)，求得l1列表中一共有多少个字符：'e'。确定循环次数
    pos1 = l1.index(s,pos1)  #从pos1的位置开始，查找'e'字符的下标
    print pos1
    pos1 += 1  #对于列表中有多个字符'e'存在的情况，为避免重复查找，要更新查找的开始下标

print '\n'

# 或者
pos2 = 0 
for i in range(l1.count(s)):
    if pos2 == 0: #从下标0开始查找，则不用修改开始下标。为避免查找的字符刚好位于0下标，需要这个判断
        pos2 = l1.index(s)
    else:  
        pos2 = l1.index(s,pos2+1)  #为避免重复查找，要更新查找的开始下标
    print pos2

print '\n'


# 方法二
first_pos = 0
for i in range(l1.count(s)):
    next_list = l1[first_pos:]  #截断列表，并赋给新列表
    print first_pos + next_list.index(s)  #输出查找出的下标。注意要加上first_pos
    next_pos = next_list.index(s) + 1  #确定下一个开始查找的下标
    first_pos += next_pos   #每次都要更新first_pos

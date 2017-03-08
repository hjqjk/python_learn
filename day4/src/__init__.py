#!/usr/bin/env python
#_*_ coding:utf8 _*_

from role import Role
from story import Story

if __name__ == '__main__':
    r1 = Role('John',18,'男',None,'学生',0) #创建角色
    r2 = Role('Liz',18,'女',None,'学生',0)
    
    story = Story(r1,r2)  #创建故事对象
    print Story.intro #打印故事简介
    story.begin() #故事开始
    story.interview() #面试
    story.separate() #分手
    story.struggle() #奋斗
    story.end()  #故事结局
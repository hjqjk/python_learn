#!/usr/bin/env python
#_*_ coding:utf8 _*_
import time

class Story(object):
    intro = 'John和Liz是高中同学时的恋人，他们一起度过了欢快的高中时光，现在面临高考...'  #故事简介，定义为静态字段
    
    def __init__(self,role1,role2):
        self.roleA = role1
        self.roleB = role2
    
    def wait_time(self,seconds):  #等待时间(秒)
        time.sleep(seconds)

    def begin(self): #故事开始
        self.wait_time(2)
        print '\n\t--- 高考结束，成绩出炉  ---\n'
        self.wait_time(1.5)
        print "%s:%s,我考上北京城市学院，好开心~~~" % (self.roleB.name,self.roleA.name)
        self.wait_time(1.5)
        print "%s:我失败了。。。" % (self.roleA.name)
        self.wait_time(1.5)
        print "%s:啊..." % (self.roleB.name)
        self.wait_time(1.5)
        print "%s:别担心，我想过了，我到北京找工作去，供你读大学。" % (self.roleA.name)
        self.wait_time(1.5)
        print "%s:真的吗？你对我真好!" % (self.roleB.name)
        self.wait_time(1.5)
        print "%s:为了你，这一切都值得!" % (self.roleA.name)
        self.wait_time(1.5)
        print "%s:%s..." % (self.roleB.name,self.roleA.name)
        
    def interview(self):  #面试阶段
        self.wait_time(2)
        print '\n\t--- 高考过后，John去北京面试 ---\n'
        self.wait_time(1.5)
        print "面试官:你学过网络吗？"
        self.wait_time(1.5)
        print "%s:没有系统学过。但是我会压水晶头，会修电脑，会装window系统。" % (self.roleA.name)
        self.wait_time(1.5)
        print "面试官:看你骨骼惊奇，就你了。什么时候能来上班？"
        self.wait_time(1.5)
        print "%s:真的吗？我随时都可以。" % (self.roleA.name)
        self.wait_time(1.5)
        print "面试官:那就下周一过来吧。"
            
    def separate(self):  #分手
        self.wait_time(2)
        print '\n\t--- 4年后 ---\n'
        self.wait_time(1.5)
        print "Liz毕业后参加工作，遇到了公司的高富帅Peter，被他吸引住了。"
        self.wait_time(1.5)
        print "一段时间后，Liz和Peter苟且在了一起。但Liz没有跟John说，仍然接受John给的钱。"
        self.wait_time(1.5)
        print "慢慢的，John发现了，他很伤心..."
        self.wait_time(1.5)
        print '''John看着手机怎么办才好？
        1、打给Liz
        2、不打 '''
        while True:
            choice = raw_input('输入选择：')
            if choice == '1':
                self.wait_time(1.5)
                print 'John质问Liz关于Peter的事，两人吵开了，最后闹得分手了。'
                break
            elif choice == '2':
                self.wait_time(1.5)
                print 'John默默忍受着，想等Liz回心转意...'
                self.wait_time(1.5)
                print '但,最后Liz还是跟他分手了。'
                break
            else:
                print '输入错误，请重新输入~'
        
    def struggle(self):
        self.wait_time(2)
        print '\n\t--- 分手后 ---\n'
        self.wait_time(1.5)
        print 'John伤心了很长时间，Liz选择了高富帅，而自己只是个穷屌丝。'
        self.wait_time(1.5)
        print 'John很不甘心，势必要逆袭！'
        print '''John考虑的两个方向：
        1、参加自考，参加Python培训班。
        2、创业'''
        while True:
            choice = raw_input('输入选择：')
            if choice == '1':
                self.wait_time(1.5)
                print '若干年后...'
                self.wait_time(2)
                print 'John当上了某大型互联网公司的IT总监，月薪5万，北京买了车和房。'
                break
            elif choice == '2':
                self.wait_time(1.5)
                print '若干年后...'
                self.wait_time(2)
                print 'John经过艰辛的打拼，终于创业成功，并北京买了车和房。'
                break
            else:
                print '输入错误，请重新输入~'
        
    def end(self):
        self.wait_time(2)
        print '\n\t--- 尾声 ---\n'
        self.wait_time(1.5)
        print 'John偶然又见到Liz,此时她已被高富Peter甩了。'
        self.wait_time(1.5)
        print 'Liz提出再回到John身边时， John优雅的说:'
        self.wait_time(1.5)
        print '''
        1、我还是喜欢粉木耳。
        2、虽然木耳已黑，但是姿势解锁了很多。'''
        while True:
            choice = raw_input('输入选择：')
            if choice == '1':
                self.wait_time(1.5)
                print 'John拒绝Liz后，一个夏日的午后，遇到了自己的真爱...'
                break
            elif choice == '2':
                self.wait_time(1.5)
                print 'John重新接受Liz后，Liz很感动，整日和John滚床单...'
                break
            else:
                print '输入错误，请重新输入~'
        
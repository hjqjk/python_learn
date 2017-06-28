#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from sendmail import SendEmail

if __name__ == '__main__':
    se = SendEmail()
    # se.sendmail_Text('批量发邮件...试版...', '<html><body><h1>Hello</h1>' +
    # '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    # '</body></html>','html')

    # se.sendmail_Accessory('测试发附件111113331',"发附件，测试，附件是图片666",'/Users/huangjunqi/管理提供资料.txt')
    # se.sendmail_Accessory('测试发附件111111999',"发附件，测试，附件是图片666",'/Users/huangjunqi/test.txt')
    se.sendmail_Accessory('测试发附件11111222222',"发附件，测试，附件是图片666",'/Users/huangjunqi/Downloads/crond实现邮件告警.pdf')
    # se.sendmail_Accessory('测试发附件22222999',"发附件，测试，附件是图片666",'/Users/huangjunqi/git_hjq/hexo_blog/source/uploads/avatar.jpeg')
#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 相关模块
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.utils import parseaddr,formataddr
from email import encoders
import smtplib
import mimetypes
import os

class SendEmail:
    def __init__(self):
        # Email 发件人地址和密码
        self.from_addr = 'message@18touch.com'
        self.password = 'pwd2015.'

        # SMTP 服务器地址
        self.smtp_server = 'smtp.exmail.qq.com'

        # 收件人地址（要批量发送，只需将收件人地址添加到这个列表）
        self.to_addr = ['huangjunqi@18touch.com','huangjunqi@leiphone.com','hjqjk123@163.com']

    # 格式化邮件地址
    def _format_addr(self,s):
        name,addr = parseaddr(s)
        # 若有中文，需要通过Header对象进行编码
        return formataddr((Header(name,'utf-8').encode(),\
                           addr.encode('utf-8') if isinstance(addr,unicode) else addr))

    # 邮件发送过程
    def sendmail(self,msg):
        try:
            # smtp协议默认端口是25
            server = smtplib.SMTP(self.smtp_server,25)
            # server.set_debuglevel(1)   # 打印发邮件的详细过程，方便调试和理解邮件原理
            server.login(self.from_addr,self.password)
            server.sendmail(self.from_addr,self.to_addr,msg.as_string())  # as_string()把MIMEText对象变成str
            server.quit()
            return True
        except Exception,e:
            print str(e)  # 打印错误信息
            return False

    # 发送邮件（文本、HTML）
    def sendmail_Text(self,subject,body,subtype):
        if subtype == 'plain':
            # 构建MIMEText对象
            msg = MIMEText(body,'plain','utf-8')
        elif subtype == 'html':
            msg = MIMEText(body, 'html', 'utf-8')
        else:
            print "类型出错，应选择：plain 或者 html"
            return False

        # 添加From、To和Subject信息到MIMEText中
        msg['From'] = self._format_addr(u'<%s>' % self.from_addr)
        msg['To'] = self._format_addr(u'<%s>' % ','.join(self.to_addr))
        msg['Subject'] = Header(subject,'utf-8').encode()

        # 发邮件
        return self.sendmail(msg)

    # 发送邮件（附件，如txt、pdf、图片等）
    def sendmail_Accessory(self, subject, body, filepath):

        # 构造MIMEMultipart邮件对象为根容器
        msg = MIMEMultipart()

        # 添加From、To和Subject信息到MIMEText中
        msg['From'] = self._format_addr(u'<%s>' % self.from_addr)
        msg['To'] = self._format_addr(u'<%s>' % ','.join(self.to_addr))
        msg['Subject'] = Header(subject, 'utf-8').encode()

        # 往邮件MIMEMultipart对象里添加MIMEText作为邮件正文，指定编码为utf-8，防止中文乱码
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        file_type, file_format = mimetypes.guess_type(filepath)[0].split('/', 1) # 根据 guess_type方法判断文件的类型和格式
        file_name = os.path.basename(filepath) # 获取文件名

        # 添加附件就是加上一个MIMEBase，读取附件信息
        with open(filepath, 'rb') as f:
            # 设置附件的MIME和文件名，指定文件类型
            mime = MIMEBase(file_type, file_format, filename=file_name)

            # 加上必要的头信息
            # 如果附件名称含有中文, 则 filename 要转换为gb2312编码, 否则附件名称就会出现乱码
            # unicode转换方法:  basename.encode('gb2312')
            # utf-8转换方法:    basename.decode('utf-8').encode('gb2312')
            mime.add_header('Content-Disposition', 'attachment; filename="%s"' % file_name.decode('utf8').encode('gb2312'))
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')

            # 把附件的内容读进来
            mime.set_payload(f.read())
            # 用Base64编码格式化
            encoders.encode_base64(mime)

            # 添加到MIMEMultipart
            msg.attach(mime)

        # 发邮件
        return self.sendmail(msg)

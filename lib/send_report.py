#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""发送测试报告"""

__author__ = 'kejie'


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from lib import parse_config
import os
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 发送邮件
def send_mail(file):
    mail_host = parse_config('mail', 'host')
    mail_user = parse_config('mail', 'login')['userId']
    mail_pass = parse_config('mail', 'login')['password']
    sender = parse_config('mail', 'sender')
    receivers = parse_config('mail', 'receivers')

    message = MIMEMultipart('alternative')

    with open(file, 'rb') as f:
        mail_msg = f.read()

    message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    att = MIMEText(mail_msg, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="{}"'.format(os.path.basename(file))
    message.attach(att)
    message['From'] = _format_addr(sender)  # 发送者
    message['To'] = ','.join([_format_addr(i) for i in receivers])  # 接收者
    subject = 'ynoteios test report'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    send_mail(os.path.join(os.path.pardir, 'result', 'ExampleReport.html'))

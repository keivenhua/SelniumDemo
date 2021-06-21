"""
自动化接口测试框架入口，只需访问该文件即可
完成的事情：
获取所有的测试用例
执行测试用例生成测试报告
将测试报告以邮件的方式进行发送
"""
import os
import smtplib
import unittest

import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from plugins.HTMLTestRunnerPlugins import HTMLTestRunner


def find_suit(suit_path,rule):
    """
    找到对应的所有测试用例
    :param suit_path:
    :param rule:
    :return:
    """
    discover = unittest.defaultTestLoader.discover(start_dir=suit_path,
                                        pattern=rule,
                                        top_level_dir=None)
    return discover

def create_reports(suites,report_path):
    # 获取文件句柄
    # 准备文件的路径
    filename = time.strftime("%Y%m%d-%H%M%S-%p") + "_report.html"
    filepath = os.path.join(report_path,filename)
    file_fp = open(filepath,"wb")
    runner = HTMLTestRunner(title="自动化测试报告",
                   description="自动化接口测试报告",
                   retry=0,
                   verbosity=2,
                   stream=file_fp)
    runner.run(suites)
    file_fp.close()
    return filepath

def send_mail(smtp_user,smtp_password,recieve_user,subject,report_path,smtp_server = "smtp.163.com",smtp_port = 465,):

    # 容器中添加附件
    filename = report_path    #附件路径
    with open(filename, "rb") as fp:
        file_body = fp.read()

    # 附件代码行
    mime_message = MIMEMultipart()

    # 容器中添加文本
    text = MIMEText(_text=file_body, _subtype="html", _charset="utf-8")
    # 将文本添加到容器里面
    mime_message.attach(text)

    file_mesage = MIMEText(_text=file_body, _subtype="base64", _charset="utf-8")
    # 额外设置
    file_mesage["Content-Type"] = "application/octet-stream"
    file_mesage["Content-Disposition"] = "attachment; filename = '{}'".format(os.path.basename(filename))
    mime_message.attach(file_mesage)

    mime_message["from"] = smtp_user
    mime_message["to"] = ";".join(recieve_user)
    mime_message["subject"] = subject

    # =============发送邮件代码行===========
    # 创建对象
    smtp = smtplib.SMTP_SSL()
    # 链接服务器
    smtp.connect(host=smtp_server, port=smtp_port)
    # 登录
    smtp.login(user=smtp_user, password=smtp_password)
    # 发送
    smtp.sendmail(from_addr=mime_message["from"], to_addrs=mime_message["to"], msg=mime_message.as_string())
    # 退出
    smtp.quit()



if __name__ == '__main__':
    # 1获取所有测试用例
    # 需要指定测试用例所在的路径（据对路径）__file__
    # print(os.path.dirname(os.path.realpath(__file__)))
    # dirname项目目录获取
    base_dir = os.path.dirname(os.path.realpath(__file__))
    # 获取用例路径
    suit_path = os.path.join(base_dir,"test_suit")
    # 调用测试用例管理函数
    rule = "test_*.py"
    suites = find_suit(suit_path,rule=rule)


    # 执行测试用例生成测试报告
    report_path = os.path.join(base_dir,"reports")
    report_filename = create_reports(suites,report_path)
    # print(report_filename)

    # 将测试报告以邮件的方式发送
    smtp_server = "smtp.163.com"
    smtp_port = 465
    smtp_password = "SFRMNDWXPRMWFGGD"
    smtp_user = "keivenhua@163.com"
    subject = "自动化接口测试报告"
    recieve_user = ["keivenhua@163.com"]

    # 发送
    send_mail(smtp_user=smtp_user,
              smtp_password=smtp_password,
              recieve_user=recieve_user,
              subject=subject,
              report_path=report_filename)
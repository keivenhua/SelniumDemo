"""
获取所有测试用例
执行测试用例生成测试报告
将测试报告以邮件形式发送
"""

import os
import smtplib
import unittest

import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from plugins.HTMLTestRunnerPlugins import HTMLTestRunner

def find_suits(suit_path,rule):
    """
    导入所有测试用例
    :param suit_path: 用例路径
    :param rule: 检索用例规则
    :return: 返回测试用例
    """
    discover = unittest.defaultTestLoader.discover(start_dir=suit_path,
                                        pattern=rule,
                                        top_level_dir=None)
    return discover

def create_reports(suites,report_path):
    """
    执行用例并生成测试报告
    :param suites: 测试用例
    :param report_path: 测试报告目录
    :return: 返回测试报告的路径
    """
    file_name = time.strftime("%y%m%d_%H%M%S_%p")+"_report.html"
    file_path = os.path.join(report_path,file_name)
    file_fp = open(file_path,"wb")
    runner = HTMLTestRunner(title="测试报告",
                   description="自动化接口测试报告",
                   retry=0,
                   verbosity=2,
                   stream=file_fp)

    runner.run(suites)
    file_fp.close()
    return file_path

def send_mail(smtp_user,smtp_password,subject,report_path,recieve_user,smtp_server = "smtp.163.com",smtp_port = 465):

    filename = report_path

    with open(filename, "rb") as fp:
        file_body = fp.read()

    mime_message = MIMEMultipart()
    text = MIMEText(_text=file_body, _subtype="html", _charset="utf-8")
    mime_message.attach(text)


    file_message = MIMEText(_text=file_body, _subtype="base64", _charset="utf-8")
    file_message["Content-Type"] = "application/octet-stream"
    file_message["Content-Disposition"] = 'attachment; filename="{}"'.format(os.path.basename(filename))
    mime_message.attach(file_message)

    mime_message["from"] = smtp_user
    mime_message["to"] = recieve_user
    mime_message["subject"] = subject

    smtp = smtplib.SMTP_SSL()
    smtp.connect(host=smtp_server, port=smtp_port)
    smtp.login(user=smtp_user, password=smtp_password)
    smtp.sendmail(from_addr=mime_message["from"], to_addrs=mime_message["to"], msg=mime_message.as_string())
    smtp.quit()


if __name__ == '__main__':
    # 获取所有的测试用例
    # 需要指定测试用例的路径
    base_dir = os.path.dirname(os.path.realpath(__file__))#项目根目录
    suit_path = os.path.join(base_dir,"test_suit")
    rule = "test_*.py"
    suits = find_suits(suit_path,rule)

    # 执行测试用例，生成测试报告
    report_pahth = os.path.join(base_dir,"reports")
    report_filename = create_reports(suits,report_pahth)
    print(report_filename)

    # 将测试报告以邮件形式发送到邮箱
    smtp_server = "smtp.163.com"
    smtp_port = 465
    smtp_user = "keivenhua@163.com"
    smtp_password = "SFRMNDWXPRMWFGGD"
    subject = "自动化接口测试报告0904"
    recieve_user = "keivenhua@163.com"

    # 发送
    send_mail(smtp_user=smtp_user,
              smtp_password=smtp_password,
              recieve_user=recieve_user,
              subject=subject,
              report_path=report_filename)
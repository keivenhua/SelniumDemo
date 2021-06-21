import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "smtp.163.com"
smtp_port = 465

#   授权码
smtp_password = "SFRMNDWXPRMWFGGD"
smtp_user = "keivenhua@163.com"

# ==============邮件内容=============
recieve_user = ["keivenhua@outlook.com","keivenhua@163.com"]
subject = "自动化测试报告"
body = "163邮箱测试报告"

# 附件代码行
mime_message = MIMEMultipart()

# 容器中添加文本
text = MIMEText(_text=body,_subtype="plain",_charset="utf-8")
# 将文本添加到容器里面
mime_message.attach(text)
# 容器中添加附件
filename = "./report.html"
with open(filename,"rb") as fp:
    file_body = fp.read()
    fp.close()

file_mesage = MIMEText(_text=file_body,_subtype="base64",_charset="utf-8")
# 额外设置
file_mesage["Content-Type"] = "application/octet-stream"
file_mesage["Content-Disposition"] = "attachment; filename = 'report.html'"
mime_message.attach(file_mesage)

mime_message["from"] = smtp_user
mime_message["to"] = ";".join(recieve_user)
mime_message["subject"] = subject


# =============发送邮件代码行===========
# 创建对象
smtp = smtplib.SMTP_SSL()
# 链接服务器
smtp.connect(host=smtp_server,port=smtp_port)
# 登录
smtp.login(user=smtp_user,password=smtp_password)
# 发送
smtp.sendmail(from_addr=mime_message["from"],to_addrs=mime_message["to"],msg=mime_message.as_string())
# 退出
smtp.quit()
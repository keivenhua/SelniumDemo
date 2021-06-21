import smtplib
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

message = MIMEText(_text=body,_subtype="plain",_charset="utf-8")
message["from"] = smtp_user
message["to"] = ";".join(recieve_user)
# message["to"] = "keivenhua@163.com"
message["subject"] = subject


smtp = smtplib.SMTP_SSL()
smtp.connect(host=smtp_server,port=smtp_port)
smtp.login(user=smtp_user,password=smtp_password)
smtp.sendmail(from_addr=message["from"],to_addrs=message["to"],msg=message.as_string())
smtp.quit()
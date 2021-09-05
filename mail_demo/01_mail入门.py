from email.mime.text import MIMEText
import smtplib

smtp_server = "smtp.163.com"
smtp_port = 465


smtp_user = "keivenhua@163.com"
smtp_password = "SFRMNDWXPRMWFGGD"


recieve_user = "keivenhua@163.com"
subject = '0902邮箱配置测试'
body = "kevinhu TEST"


message = MIMEText(_text=body,_subtype="plain",_charset="utf-8")
message["from"] = smtp_user
message["to"] = recieve_user
message["subject"] = subject

smtp = smtplib.SMTP_SSL()
smtp.connect(host=smtp_server,port=smtp_port)
smtp.login(user=smtp_user,password=smtp_password)
smtp.sendmail(from_addr=message["from"],to_addrs=message["to"],msg=message.as_string())
smtp.quit()

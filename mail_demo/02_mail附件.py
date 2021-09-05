from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

smtp_server = "smtp.163.com"
smtp_port = 465


smtp_user = "keivenhua@163.com"
smtp_password = "SFRMNDWXPRMWFGGD"


recieve_user = "keivenhua@163.com"
subject = '0902邮箱配置测试'
body = "发送附件成功"

mime_message = MIMEMultipart()
text = MIMEText(_text=body,_subtype="plain",_charset="utf-8")
mime_message.attach(text)

filename = "./report.html"
with open(filename,"rb") as fp:
    file_body = fp.read()
file_message = MIMEText(_text=file_body,_subtype="base64",_charset="utf-8")
file_message["Content-Type"] = "application/octet-stream"
file_message["Content-Disposition"] = 'attachment; filename="report.html"'
mime_message.attach(file_message)

mime_message["from"] = smtp_user
mime_message["to"] = recieve_user
mime_message["subject"] = subject

smtp = smtplib.SMTP_SSL()
smtp.connect(host=smtp_server,port=smtp_port)
smtp.login(user=smtp_user,password=smtp_password)
smtp.sendmail(from_addr=mime_message["from"],to_addrs=mime_message["to"],msg=mime_message.as_string())
smtp.quit()

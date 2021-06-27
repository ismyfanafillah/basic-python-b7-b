import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "email@gmail.com"
receivers = ["email@gmail.com"]

message = MIMEText("hello", "plain")
message ["from"] = Header("email")
message ["to"] = Header("email")

subject = "Python SMTP TES EMAIL"
message ["subject"] = Header(subject)

try:
    smtp0bj = smtplib.SMTP("localhost")
    smtp0bj.sendmail(sender, receivers, message.as_string())
    print ("Email berhasil dikirim")
except smtplib.SMTPException:
    print ("Error: kesalahan")

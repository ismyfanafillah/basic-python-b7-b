import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pprint import pprint

sender = "sender_email@gmail.com"
with open("receivers_list.txt","r") as f:
    receivers = f.read().split(',')
#receivers =["email1@gmail.com", "email2@gmail.com", "email3@gmail.com"] #klo ga pakai receivers_list.txt, pakai ini

#pprint(receivers)
message = MIMEMultipart()

message ["from"] = sender
message ["to"] = ','.join( receivers )
message ["subject"] = "hello"

body = "smooth like butter"

message.attach(MIMEText(body, "plain"))

filename = "ini contoh.jpg" #nama file yang akan dikirim
attachment = open(r"C:\Users\ASUS\Pictures\bg.JPEG", "rb") #file yang akan dikirim

part = MIMEBase("applicaton", "octet-stream")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header("content-disposition", "attachment; filename= %s" % filename)

message.attach(part)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login (sender,"password")
text = message.as_string()
server.sendmail (sender, receivers, text)
server.quit()

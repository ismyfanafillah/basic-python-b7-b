import smtplib

server = smtplib.SMTP_SSL ("smptp.gmail.com", 465)

server.login ("email@gmail.com","password")
server.sendmail ("emailfrom@gmail.com", 
                "emailto@gmail.com",
                "Hello")

server.quit ()
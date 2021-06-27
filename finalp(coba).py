import smtplib

server = smtplib.SMTP_SSL ("smptp.gmail.com", 465)

server.login ("ismyfanafillah@gmail.com","password")
server.sendmail ("ismyfanafillah@gmail.com", 
                "ismyff173@gmail.com",
                "Hello")

server.quit ()
import smtplib

HOST = "smtp.163.com"
SUBJECT = "Test email from Python"
TO = "2480621579@qq.com"
FROM = "liupan6888@163.com"
text = "Python rules them all!"
BODY = '\r\n'.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
))
server = smtplib.SMTP()
server.connect(HOST, "25")
# server.starttls()
server.login("liupan6888@163.com", "password")
server.sendmail(FROM, [TO], BODY)
server.quit()

import smtplib

sender = 'wdsgh@hotmail.com'
receivers = ['sgh1982@gmail.com']

message = """From: SGH <wdsgh@hotmail.com>
To: SGH <sgh1982@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message."""

try:
    smtpObj = smtplib.SMTP('loalhost')
    smtpObj.sendmail(sender, receivers, message)
    print "Email sent successfully"
except Exception:
    print "Error: unable to send email"
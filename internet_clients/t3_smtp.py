# -*- coding: UTF-8 -*-

from smtplib import SMTP

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'me@hotmail.com'
msg['To'] = 'you@gmail.com'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = SMTP('smtp-mail.outlook.com',587)
# identify ourselves to smtp hotmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('me@hotmail.com', 'secret')

errs = mailserver.sendmail('me@hotmail.com', ['you@gmail.com'], msg.as_string())

mailserver.quit()

print 'mail sent.'

#assert len(errs) == 0, errs

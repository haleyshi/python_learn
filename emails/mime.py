# -*- coding: UTF-8 -*-

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello World!\r\n', 'plain')
    email.attach(text)
    html = MIMEText('<html><body><h4>Hello World!</h4></body></html>', 'html')
    email.attach(html)
    return email

def make_image_msg(fn):
    f = open(fn, 'rb')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)

    #email = MIMEMultipart()

    #msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % (fn, fn), 'html')
    #email.attach(msgText)  # Added, and edited the previous line

    #img = MIMEImage(data)
    #img.add_header('Content-ID', '<{}>'.format(fn))
    #email.attach(img)

    return email

def sendMsg(fr, to, msg):
    mailserver = SMTP('smtp-mail.outlook.com', 587)
    # identify ourselves to smtp hotmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('wdsgh@hotmail.com', 'xxxxxx')
    errs = mailserver.sendmail(fr, to, msg)
    mailserver.quit()


if __name__ == '__main__':
    SENDER = 'wdsgh@hotmail.com'
    RECIPS = ['wdsgh@hotmail.com', 'sgh1982@gmail.com']
    IMG_FILE_PATHNAME = 'Koala.jpg'

    print 'Sending multipart alternative msg...'
    msg = make_mpa_msg()
    msg['From'] = SENDER
    msg['To'] = ', '.join(RECIPS)
    msg['Subject'] = 'multipart alternative test'
    sendMsg(SENDER, RECIPS, msg.as_string())
    print '...mail sent.'

    print
    print 'Sending image msg...'
    msg = make_image_msg(IMG_FILE_PATHNAME)
    msg['From'] = SENDER
    msg['To'] = ', '.join(RECIPS)
    msg['Subject'] = 'image file test'
    sendMsg(SENDER, RECIPS, msg.as_string())
    print '...mail sent.'
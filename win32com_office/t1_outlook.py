# -*- coding: UTF-8 -*-

'''
install both pywin32.exe and python package (pip install pywin32)
'''

from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)

def outlook():
    app = 'Outlook'
    outlook = win32.gencache.EnsureDispatch('%s.Application' % app)  #静态调度
    #outlook = win32.Dispatch('%s.Application' % app)  #动态调度
    email = outlook.CreateItem(win32.constants.olMailItem)
    recip = email.Recipients.Add('sgh1982@gmail.com')
    subj = email.Subject = 'Python-to-%s Demo' % app
    body = ["Line %d" % i for i in RANGE]
    body.insert(0, '%s\r\n' % subj)
    body.append("\r\nThat's all folks!")
    email.Body = '\r\n'.join(body)
    email.Send()

    ns = outlook.GetNamespace('MAPI')
    outbox = ns.GetDefaultFolder(win32.constants.olFolderOutbox)
    outbox.Display()
    outbox.Items.Item(1).Display()

    warn(app)
    outlook.Quit()


if __name__ == '__main__':
    Tk().withdraw()  # 不让Tk顶级窗口出现
    outlook()
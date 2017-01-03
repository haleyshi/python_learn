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

def excel():
    app = 'Excel'
    #xl = win32.gencache.EnsureDispatch('%s.Application' % app)  #静态调度
    xl = win32.Dispatch('%s.Application' % app)  #动态调度
    ss = xl.Workbooks.Add()
    sh = ss.ActiveSheet
    xl.Visible = True
    sleep(1)

    sh.Cells(1, 1).Value = 'Python-to-%s Demo' % app
    sleep(1)

    for i in RANGE:
        sh.Cells(i, 1).Value = 'Line %d' % i
        sleep(1)

    sh.Cells(i+2, 1).Value = "That's all folks!"

    warn(app)
    ss.Close(False)
    xl.Application.Quit()


if __name__ == '__main__':
    Tk().withdraw()  # 不让Tk顶级窗口出现
    excel()
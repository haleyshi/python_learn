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

def word():
    app = 'Word'
    word = win32.gencache.EnsureDispatch('%s.Application' % app)  #静态调度
    #word = win32.Dispatch('%s.Application' % app)  #动态调度
    doc = word.Documents.Add()
    word.Visible = True
    sleep(1)

    rng = doc.Range(0,0)
    rng.InsertAfter('Python-to-%s Demo\r\n\r\n' % app)
    sleep(1)

    for i in RANGE:
        rng.InsertAfter('Line %d\r\n' % i)
        sleep(1)

    rng.InsertAfter("\r\nThat's all folks!\r\n")

    warn(app)
    doc.Close(False)
    word.Application.Quit()


if __name__ == '__main__':
    Tk().withdraw()  # 不让Tk顶级窗口出现
    word()
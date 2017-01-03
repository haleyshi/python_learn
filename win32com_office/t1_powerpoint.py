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

def ppt():
    app = 'PowerPoint'
    ppt = win32.gencache.EnsureDispatch('%s.Application' % app)  #静态调度
    #ppt = win32.Dispatch('%s.Application' % app)  #动态调度
    slides = ppt.Presentations.Add()
    ppt.Visible = True

    s1 = slides.Slides.Add(1, win32.constants.ppLayoutText)
    sleep(1)
    s1a = s1.Shapes(1).TextFrame.TextRange
    s1a.Text = 'Python-to-%s Demo' % app
    sleep(1)

    s1b = s1.Shapes(2).TextFrame.TextRange
    for i in RANGE:
        s1b.InsertAfter('Line %d\r\n' % i)
        sleep(1)

    s1b.InsertAfter("\r\nThat's all folks!")

    warn(app)
    slides.Close()
    ppt.Quit()


if __name__ == '__main__':
    Tk().withdraw()  # 不让Tk顶级窗口出现
    ppt()
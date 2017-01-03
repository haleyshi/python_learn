# -*- coding: UTF-8 -*-

'''
install both pywin32.exe and python package (pip install pywin32)
'''

from Tkinter import Tk
from time import sleep, ctime
from tkMessageBox import showwarning
import win32com.client as win32
from urllib import urlopen

warn = lambda app: showwarning(app, 'Exit?')
TICKS = ('ERIC', 'ERIC-B.ST', 'ERIC-A.ST')
COLS = ('TICKER', 'PRICE', 'CHG', "%AGE")
URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1clp2'

def excel():
    app = 'Excel'
    #xl = win32.gencache.EnsureDispatch('%s.Application' % app)  #静态调度
    xl = win32.Dispatch('%s.Application' % app)  #动态调度
    ss = xl.Workbooks.Add()
    sh = ss.ActiveSheet
    xl.Visible = True
    sleep(1)

    sh.Cells(1, 1).Value = 'Python-to-%s Stock Quote Demo' % app
    sleep(1)

    sh.Cells(3, 1).Value = 'Price quoted as of: %s' % ctime()
    stocks = urlopen(URL % ','.join(TICKS))
    sleep(1)

    for i in range(4):
        sh.Cells(5, i+1).Value = COLS[i]
    sleep(1)

    sh.Range(sh.Cells(5, 1), sh.Cells(5, 4)).Font.Bold = True
    sleep(1)

    row = 6

    for stock in stocks:
        tick, price, dummy, chg, per = stock.split(',')
        sh.Cells(row, 1).Value = eval(tick)
        sh.Cells(row, 2).Value = ('%.2f' % round(float(price), 2))
        sh.Cells(row, 3).Value = eval(chg)
        sh.Cells(row, 4).Value = eval(per.rstrip())
        row += 1
        sleep(1)

    stocks.close()

    warn(app)
    ss.Close(False)
    xl.Application.Quit()


if __name__ == '__main__':
    Tk().withdraw()  # 不让Tk顶级窗口出现
    excel()
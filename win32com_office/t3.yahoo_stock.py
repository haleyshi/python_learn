# -*- coding: UTF-8 -*-

'''
install both pywin32.exe and python package (pip install pywin32)
'''

from Tkinter import Tk
from time import sleep, ctime
import win32com.client as win32
from urllib import urlopen

NAMES = ('ZXGA','GYLS', 'YTGF', 'ZJGK', 'ZXZQ', 'ERIC', 'ERIC-B', 'ERIC-A')
TICKS = ('000839.SZ', '600059.SS', '002284.SZ', '600895.SS', '600030.SS','ERIC', 'ERIC-B.ST', 'ERIC-A.ST')
COLS = ('NAME', 'CODE', 'PRICE', 'CURRENT', 'CHG', "%AGE")
URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1clp2'
START_ROW = 4

def excel():
    app = 'Excel'
    xl = win32.gencache.EnsureDispatch('%s.Application' % app)
    ss = xl.Workbooks.Add()
    sh = ss.ActiveSheet
    xl.Visible = True
    sleep(1)

    for i in range(6):
        sh.Cells(3, i + 1).Value = COLS[i]
    sh.Range(sh.Cells(3, 1), sh.Cells(3, 6)).Font.Bold = True
    sleep(1)

    row = START_ROW
    for name in NAMES:
        sh.Cells(row, 1).Value = name
        row += 1

    while True:
        sh.Cells(1, 1).Value = 'Price quoted as of: %s' % ctime()
        stocks = urlopen(URL % ','.join(TICKS))

        row = START_ROW
        for stock in stocks:
            tick, price, open, chg, per = stock.split(',')
            sh.Cells(row, 2).Value = eval(tick)
            try:
                sh.Cells(row, 3).Value = ('%.2f' % round(float(price), 2))
            except ValueError:
                sh.Cells(row, 3).Value = 'N/A'

            try:
                sh.Cells(row, 4).Value = eval(open)
            except NameError:
                sh.Cells(row, 4).Value = 'N/A'

            try:
                sh.Cells(row, 5).Value = eval(chg)
            except NameError:
                sh.Cells(row, 5).Value = 'N/A'

            try:
                sh.Cells(row, 6).Value = eval(per.rstrip())
            except NameError:
                sh.Cells(row, 6).Value = 'N/A'

            row += 1

        stocks.close()
        sleep(60)

if __name__ == '__main__':
    Tk().withdraw()  # 不让Tk顶级窗口出现
    excel()
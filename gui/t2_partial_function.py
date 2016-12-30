# -*- coding: UTF-8 -*-

from functools import partial as pto
from Tkinter import Tk, Button, X
from tkMessageBox import showinfo, showwarning, showerror

CRIT = 'crit'
WARN = 'warn'
INFO = 'info'

SIGNS= {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': INFO,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': INFO,
}

critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')

Button(top, text='QUIT', command=top.quit, bg='red', fg='white').pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
InfoButton = pto(MyButton, command=infoCB, bg='white')

for sign in SIGNS:
    signType = SIGNS[sign]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (signType.title(), sign, '.upper()' if signType==CRIT else '.title()')
    eval(cmd)

top.mainloop()

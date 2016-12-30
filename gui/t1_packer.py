# -*- coding: UTF-8 -*-

from Tkinter import *

def resize(ev=None):
    #print ev
    hello.config(font='Helvetica -%d bold' % scale.get())

top = Tk()
top.title('Hello')
top.geometry('250x150')   ## Window Size

hello = Label(top, text='Hello World!', font='Helvetica -12 bold')
hello.pack(fill=Y, expand=1)  # 充满空白的垂直位置

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)  # 充满空白的水平位置

quit = Button(top, text='退出！', command=top.quit, activebackground='red', activeforeground='white')
quit.pack()

mainloop()
# -*- coding: UTF-8 -*-

from Tkinter import Button, Label, END
from Tix import Tk, Control, ComboBox

top = Tk()
top.tk.eval('package require Tix')

lb = Label(top, text='Animals (in pairs; min: pair, max: dozen)')
lb.pack()

ct = Control(top, label='Number:', integer=True, max=12, min=2, value=6, step=2)
ct.label.config(font=('Helvetica', 14, 'bold'))
ct.pack()

cb = ComboBox(top, label='Type:', editable=True)
for animal in ('dog', 'cat', 'hamster', 'spider', 'python'):
    cb.insert(END, animal)
cb.pack()

qb = Button(top, text='Quit', command=top.quit, bg='red', fg='white')
qb.pack()

top.mainloop()


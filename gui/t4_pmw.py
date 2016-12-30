# -*- coding: UTF-8 -*-

from Tkinter import Button, Label, END, W
from Pmw import ComboBox, initialise, Counter

top = initialise()

lb = Label(top, text='Animals (in pairs; min: pair, max: dozen)')
lb.pack()

ct = Counter(top, labelpos=W, label_text='Number:', datatype='integer', entryfield_value=6, increment=2, entryfield_validate={'validator': 'integer', 'min': 2, 'max': 12})  ## W: West
ct.pack()

cb = ComboBox(top, labelpos=W, label_text='Type:')
for animal in ('dog', 'cat', 'hamster', 'spider', 'python'):
    cb.insert(END, animal)
cb.pack()

qb = Button(top, text='Quit', command=top.quit, bg='red', fg='white')
qb.pack()

top.mainloop()


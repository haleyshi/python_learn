__author__ = 'eguoshi'

import simplegui

g = simplegui.GUI()

def buttoncallback():
    g.status("Button clicked!")

g.button("Click me!", buttoncallback)
g.button("Click me too!", buttoncallback)

def listboxcallback(text):
    g.status("listbox select: '{0}'".format(text))

g.listbox(["One", "Two", "Three"], listboxcallback)
g.listbox(["A", "B", "C"], listboxcallback)

def scalecallback(text):
    g.status("scale value: '{0}'".format(text))

g.scale("Scale me!", scalecallback)

g.run()
from Tkinter import *

root = Tk()

languages1 = ["C", "Python", "Nodejs", "Java", "C++", "R"]
languages2 = ["html", "CSS", "JS", "JSP", "Android SDK", "Swift"]

listbox1 = Listbox(root)
listbox2 = Listbox(root)

for item in languages1:
    listbox1.insert(0, item)

for item in languages2:
    listbox2.insert(0, item)

listbox1.pack()
listbox2.pack()

root.mainloop()
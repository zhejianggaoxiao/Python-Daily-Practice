"""
-------------------------------------------------
   File Name：     011-ShowThirdFiles
   Description :
   Author :       gaox
   date：          7/19/18
-------------------------------------------------
   Change Activity:
                   7/19/18:
-------------------------------------------------
"""
__author__ = 'gaox'

import sys

from tkinter import *

app = Tk()
label = Label(text='Packages', font=('Hack', 25, 'bold'))
label.pack()
listbox = Listbox(bg='#f2f2f2', fg='red')
listbox.pack()

for item in sys.modules.keys():
    listbox.insert(END, item)

app.mainloop()
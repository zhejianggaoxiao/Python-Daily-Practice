"""
-------------------------------------------------
   File Name：     01-ShowHiddenFiles
   Description :
   Author :       gaox
   date：          7/19/18
-------------------------------------------------
   Change Activity:
                   7/19/18:
-------------------------------------------------
"""
__author__ = 'gaox'

from tkinter import *
import os

'''
## tkinter tutorial

# 创建应用对象
app = Tk()

# 创建按钮对象
btn = Button(text='click')
# 显现按钮
btn.pack()

# 运行
app.mainloop()
'''

app = Tk()

path = '/Users/gaox'
files = os.listdir(path)

# 标签框
label = Label(text='All hidden files', font=('Hack', 25, 'bold'))
label.pack()

# 列表框
listbox = Listbox(bg='#f2f2f2', fg='red')
listbox.pack(fill=BOTH, expand=True)

for f in files:
    if f.startswith('.'):
        listbox.insert(END, f)


app.mainloop()



"""
-------------------------------------------------
   File Name：     04-RunPython
   Description :
   Author :       gaox
   date：          7/20/18
-------------------------------------------------
   Change Activity:
                   7/20/18:
-------------------------------------------------
"""
__author__ = 'gaox'


import os
from runpy import run_path
from tkinter import *
from multiprocessing import Process, active_children

# |script| -> func1 -> func2 -> func3
# |app| -> update() & if do() -> update() & if do()
# =》 update 更新app的UI界面
# 如果do操作时间过长，update函数就会崩溃
# 采用多进程的方式可以解决这个问题

def make_app():
    app = Tk()
    Listbox(app, name='lsb').pack()
    Button(app, text='run', command=run_script).pack()
    Button(app, text='stop', command = stop_script).pack()
    app.geometry('300x400')
    return app

def ui_make_list():
    listb = app.children['lsb']
    for d in os.listdir('.'):
        listb.insert(END, d)

def run_script():
    listb = app.children['lsb']
    s_path = listb.get(ACTIVE)
    # 开辟新的进程
    p = Process(name='print', target = lambda: run_path(s_path))
    p.start()

def stop_script():
    # 查看活动进程
    pchild = active_children()
    for p in pchild:
        if p.name == 'print':
            p.terminate()

def watcher():
    listb = app.children['lsb']
    s_path = listb.get(ACTIVE)
    print(active_children())
    print(s_path)
    app.after(1000, watcher)


app = make_app()
app.after(100,ui_make_list)
app.after(0, watcher)
app.mainloop()
"""
-------------------------------------------------
   File Name：     05-CountDown
   Description :
   Author :       gaox
   date：          7/21/18
-------------------------------------------------
   Change Activity:
                   7/21/18:
-------------------------------------------------
"""
__author__ = 'gaox'

# Core --> Core&UI --> Core&UI&User --> Boundary.Edge.Corner（极限问题）

import time
from tkinter import *
from multiprocessing import Process
from threading import Thread, enumerate

info = {
    'total_time':60
}


def make_app():
    _font = ('Hack', 25, 'bold')
    app = Tk()
    Label(app, name = 'lb', text=0, font=_font).pack()
    Entry(app, name='ipt').pack()
    Button(app, text = '开始',name='btn', command =time_counts ).pack()
    app.geometry('300x200')
    return app

def time_counts():
    def _count():
        while info['total_time']:
            info['total_time'] -= 1
            print(info['total_time'])
            time.sleep(1)
    p = Thread(target = _count, name='timer')
    p.start()


def ui_watcher():
    def _update_button():
        btn = app.children['btn']
        timer = [t for t in enumerate() if t.name == 'timer']
        if timer:
            btn['state'] = 'disabled'
        else:
            btn['state'] = 'normal'


    def _get_time():
        ipt = app.children['ipt']
        timer = [ t for t in enumerate() if t.name=='timer']
        if not timer and ipt.get():
            info['total_time'] = int(ipt.get())

    def _update_time():
        lb = app.children['lb']
        lb.config(text=info['total_time'])

    def _main():
        while True:
            # _update_button()
            # print(enumerate())
            _get_time()
            _update_time()
            _update_button()

    t = Thread(target=_main)
    t.start()




app = make_app()
app.after(0, ui_watcher)
app.mainloop()

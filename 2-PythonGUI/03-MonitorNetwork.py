"""
-------------------------------------------------
   File Name：     03-MonitorNetwork
   Description :
   Author :       gaox
   date：          7/20/18
-------------------------------------------------
   Change Activity:
                   7/20/18:
-------------------------------------------------
"""
__author__ = 'gaox'

import psutil
import time
from tkinter import *

# # 网速监控
# while True:
#     s1 = psutil.net_io_counters(pernic = True)['en0']
#     time.sleep(1)
#     s2 = psutil.net_io_counters(pernic = True)['en0']
#     result = s2.bytes_recv - s1.bytes_recv      # unit: byte
#     print(result/1024)

# # 实时显示
# def fun1():
#     print('hi')
#     app.after(1000, fun1)
#
# app = Tk()
# app.after(1000, fun1)       # 在 GUI 1000ms之后自动执行
#
# app.mainloop()

def make_app():
    app = Tk()
    app.geometry('300x150')
    app.config(bg='#303030')
    Label(text = 'Speed Monitor',
          font = ('Hack', 25, 'bold'),
          bg= '#303030',
          fg='white').pack()

    Label(name='lb2', text='_kb/s',
          font = ('Hack', 20,'bold'),
          bg='#303030',
          fg='white').pack()
    return app



def speed_test():
    s1 = psutil.net_io_counters(pernic = True)['en0']
    time.sleep(1)
    s2 = psutil.net_io_counters(pernic = True)['en0']
    result = s2.bytes_recv - s1.bytes_recv      # unit: byte
    return str(result/1024)+' kb/s'


# 在这里不能使用 while True 无限循环操作
def ui_update(do):

    data = do()
    lb2 = app.children['lb2']
    lb2.config(text=data)
    time.sleep(1)
    app.after(1000, lambda: ui_update(do))

app = make_app()

# 程序自动触发，而不是用户手动执行
app.after(100, lambda: ui_update(speed_test))
app.mainloop()




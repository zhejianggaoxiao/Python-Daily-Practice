"""
-------------------------------------------------
   File Name：     021-ResizeTool
   Description :
   Author :       gaox
   date：          7/20/18
-------------------------------------------------
   Change Activity:
                   7/20/18:
-------------------------------------------------
"""
__author__ = 'gaox'


from PIL import Image as Img
from tkinter import *
from tkinter.filedialog import *
import os


# 全局变量
info = {
    'path':None
}
outpath = None

# 制作app
def make_app():
    app = Tk()
    Label(app, text='Image Resize Tool', font=('Hack', 25, 'bold')).pack()
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(text='Open File', command=ui_getdata).pack()
    Button(text='Output File', command=ui_outdata).pack()
    Button(text='Resize Img', command=resize_img).pack()
    app.geometry('300x500')
    return app

def ui_getdata():
    f_names = askopenfilenames()
    info['path'] = f_names
    lbox = app.children['lbox']
    if f_names:
        for name in f_names:
            lbox.insert(END, name.split('/')[-1])


def resize_img():
    f_names = info['path']
    if f_names:
        for name in f_names:
            img = Img.open(name)
            for sz in [50,100,120,180,200,300]:
                temp = img.resize((sz,sz))
                temp.save(os.path.join(outpath, str(sz)+'_'+name.split('/')[-1]))


def ui_outdata():
    # 输出路径设定：askdirectory
    global outpath
    outpath = askdirectory()


app = make_app()
app.mainloop()
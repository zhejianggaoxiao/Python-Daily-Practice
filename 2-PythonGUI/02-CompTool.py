"""
-------------------------------------------------
   File Name：     02-CompTool
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
from tkinter.filedialog import *
from PIL import Image as Img

'''
## 如何压缩图片
path='/Users/gaox/Desktop/Python实战/麻瓜教程/02 实用主义学Python图形界面开发（完结）/2. 如何做一个压缩图片的小工具/123.png'
output = '/Users/gaox/Desktop/Python实战/麻瓜教程/02 实用主义学Python图形界面开发（完结）/2. 如何做一个压缩图片的小工具/123-c.png'
image = Image.open(path)
image.save(output, quality=30)

## 点击操作
app = Tk()

def do():
    print(1)
    
# 当按钮点击的时候，执行command命令
btn = Button(text='click', command=do)
btn.pack()

app.mainloop()
'''

info = {
    'path':None
}

def make_app():
    app = Tk()
    Label(app,text='Image Compress Tool').pack()
    Listbox(app,name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app,text='open', command=ui_getdata).pack()
    Button(app,text='Compress', command=compress).pack()
    app.geometry('300x400')
    return app

def ui_getdata():
    # 弹出对话框，选取需要的文件
    f_names = askopenfilenames()
    info['path']=f_names
    lbox = app.children['lbox']
    if info['path']:
        for name in f_names:
            lbox.insert(END, name.split('/')[-1])


def compress():
    for f_path in info['path']:
        output = '/Users/gaox/Desktop/'
        name = f_path.split('/')[-1]
        image = Img.open(f_path)
        image.save(output+'c_'+name, quality=40)


app = make_app()
app.mainloop()
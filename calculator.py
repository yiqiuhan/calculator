from tkinter import *


#实例化Button，使用command选项关联一个函数，点击按钮则执行该函数
class App:
 def onclick():
    print("1")
 def __init__(self, master):
  fm1 = Frame(master)
  e=StringVar()
  entry = Entry(root,textvariable=e).pack()
  fm1.pack(side=TOP, padx=10)

  fm2 = Frame(master)
  Button(fm2, text='1').pack(side=LEFT)
  Button(fm2, text='2').pack(side=LEFT)        
  fm2.pack(side=TOP, padx=10)


#设置pack布局方式
root = Tk()
root.title("Calculator")
display = App(root)

root.mainloop()


from tkinter import*
import math

class calculator:
    def __init__(self, master):
     # 设置显式面板的变量
     self.result = StringVar()
     self.result.set(0)
     # 设置一个全局变量  运算数字和f符号的列表
     self.lists = []
     # 添加一个用于判断是否按下运算符号的标志
     self.ispresssign = False
     
     fm1 = Frame(master)
     entry1 = Entry(fm1,width=80,textvariable = "input please").grid(row=1)
     entry2 = Entry(fm1,width=80,state=DISABLED,textvariable=self.result).grid(row=2)
     fm1.grid(row=1)


     
    
     fm2 = Frame(master)
     symbols = ['%','CE','C','B','1','2','3','+','4','5','6','-','7','8','9','x','=','0','.','/']
    
     r = 0
     x=symbols[r]
     for c in symbols:
    
      a=r//4
      b=r%4
      
      x=symbols[r]
      Button(fm2,text=c, relief=RIDGE,width=15,command=lambda c=x:self.pressnum(c)).grid(row=a,column=b)
      r+=1
      print(x)
     fm2.grid(row=2)

    def pressnum(self,num):
       if num == '.':
            num = '0.'
        # 获取面板中的原有数字
       oldnum = self.result.get()
        # 判断界面数字是否为0
       if oldnum == '0':
            self.result.set(num)
       else:
            # 连接上新按下的数字
            newnum = oldnum + num
 
            # 将按下的数字写到面板中
            self.result.set(newnum)

    def presscalculate(self,sign):
        # 保存已经按下的数字和运算符号
        # 获取界面数字
        num = self.result.get()
        self.lists.append(num)
        # 保存按下的操作符号
        self.lists.append(sign)
        # 设置运算符号为按下状态
        self.ispresssign = True
root=Tk()    
root.title("calculator")
display = calculator(root)
root.mainloop()

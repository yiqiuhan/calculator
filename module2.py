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
     symbols = ['%','CE','C','←','1','2','3','+','4','5','6','-','7','8','9','*','=','0','.','/']
    
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
       if self.ispresssign == False:
            pass
        # 获取面板中的原有数字
       else:
            self.result.set(0)
            # 重置运算符号的状态
            self.ispresssign = False
       
       if num in '123456789.':

          global oldnum
          oldnum= self.result.get()
         # 判断界面数字是否为0
          if num == '.':
            num = '0.'
           
          if oldnum == '0':
            self.result.set(num)
          else:
            # 连接上新按下的数字
            newnum = oldnum + num
 
            # 将按下的数字写到面板中
            self.result.set(newnum)

       elif num in '+-*/':
         # 保存已经按下的数字和运算符号
         # 获取界面数字
         oldnum = self.result.get()
         newnum = oldnum + num
         self.lists.append(newnum)
         # 保存按下的操作符号
         #self.lists.append(num)
         # 设置运算符号为按下状态
         self.ispresssign = True

        #获取运算结果
       elif num =='=':
         # 获取所有的列表中的内容（之前的数字和操作）
         # 获取当前界面上的数字
         curnum = self.result.get()
         # 将当前界面的数字存入列表
         self.lists.append(curnum)
         # 将列表转化为字符串
         calculatestr = ''.join(self.lists)
         # 使用eval执行字符串中的运算即可
         endnum = eval(calculatestr)
         # 将运算结果显示在界面中
         self.result.set(str(endnum)[:10])
         if self.lists != 0:
            self.ispresssign = True
         # 清空运算列表
         self.lists.clear()

        #←按键功能
       elif num=='←':
         if self.result.get() == '' or self.result.get() == '0':
            self.result.set('0')
            return
         else:
            num = len(self.result.get())
            if num > 1:
                strnum = self.result.get()
                strnum = strnum[0:num - 1]
                self.result.set(strnum)
            else:
                self.result.set('0')
        #C按键功能            
       elif num=='C':
           self.lists.clear()
           self.result.set(0)
root=Tk()    
root.title("calculator")
display = calculator(root)
root.mainloop()
mycalculator=calaulator()

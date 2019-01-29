from tkinter import *

class calculator:
    def __init__(self, master):
     fm1 = Frame(master)
     entry1 = Entry(fm1,width=80,textvariable = "input please").grid(row=1)
     entry2 = Entry(fm1,width=80,state=DISABLED).grid(row=2)
     fm1.grid(row=1)

    
     fm2 = Frame(master)
     symbols = ['1','2','3','+','4','5','6','-','7','8','9','x','=','0','.','/']
 
     r = 0
     for c in symbols:
    
      a=r//4
      b=r%4
      def onclick():
        print("1")
      Button(fm2,text=c, relief=RIDGE,width=15,command=onclick).grid(row=a,column=b)
      r = r + 1
     fm2.grid(row=2)
     
root=Tk()    
root.title("calculator")
display = calculator(root)
root.mainloop()

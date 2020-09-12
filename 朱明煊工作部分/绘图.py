import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("Combobox下拉框")
win.geometry("800x600+600+100")

cv= tkinter.StringVar()
com=ttk.Combobox(win,textvariable=cv)
com.pack()
#设置下拉数据
com["value"]=("福建","江西","浙江")

#设置默认值
com.current(0)

#绑定事件
def func(event):
    print(com.get())
    print(cv.get())
    print("tom is a boy")
com.bind("<<ComboboxSelected>>",func) #等同于textvariable=cv这个变量
from tkinter import *
import tkinter
import pyautogui
import pyperclip
import time

def gg(text,time_1,number):

     time.sleep(2)#等待时间

     for s in range(1,number):

          for i in text.split("/n") * 99:
               # split("/n")把文章分成一句一句的
               print(i)
               # 提取坐标，通俗一点就是鼠标点一下这个位置,定位聊天窗口
               pyperclip.copy(i)
               # 复制到截切版上去
               pyautogui.hotkey("ctrl", "v")
               # 粘贴
               pyautogui.typewrite("\n")
               time.sleep(time_1)
               break

def open():

     text = z.get()
     time_1 = float(x.get())
     number = int(c.get())
     gg(text,time_1,number)


root = Tk()
root.config(bg='#87CEEB')
root.title("轰你妹!")

root.geometry('450x260+700+300')

tkinter.Label(root,text="语句：").place(x=5, y=25, width=90, height=40)
z = tkinter.Entry(root)
z.place(x=100, y=25, width=340, height=40)

tkinter.Label(root,text="语速：").place(x=5, y=85, width=90, height=40)
x = tkinter.Entry(root)
x.place(x=100, y=85, width=340, height=40)

tkinter.Label(root,text="次数：").place(x=5, y=145, width=90, height=40)
c = tkinter.Entry(root)
c.place(x=100, y=145, width=340, height=40)

an = tkinter.Button(root,text="确认",bg='#7CCD7C',height=40,width=90,command=open)
an.place(x=230, y=205, width=200, height=40)

tkinter.Label(root,text="准备时间2秒！").place(x=20, y=205, width=180, height=40)

root.resizable(0, 0)#固定窗口
# 显示窗口
root.mainloop()

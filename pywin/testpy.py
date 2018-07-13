#!/usr/bin/python
## _*_ coding:UTF-8 _*_
#运行命令cmd /k C:/python3.6.6/python.exe "D:\pyFiles\pywin32test.py" & ECHO. & PAUSE & EXIT
#加入ctypes库，用于调用动态链接库函数的功能模块，一定程度上可以用于Python与其他语言的混合编程
import os
#导入pywin32库
import win32api
import win32con
import win32gui
#导入数学工具包
import math
#导入时间戳工具
import time
#导入方式1，导入自定义模块，注意，这里是导入这个模块文件
#import mouse
#导入方式2，这里是导入模块文件的内容
from mouse import *



#找到窗口句柄，（窗口类名，窗口名），窗口名为None表示只通过窗口类名找到窗口的句柄，返回的是个句柄包装类
handle = win32gui.FindWindow("notepad", None)
#得到句柄包装类的十进制值，没找到句柄返回0
hwnd = handle.__int__()
print("句柄十进制：",hwnd)
hwnd = 264070
x = 300
y = 250

#导入方式1，产生实例的方式：在导入自定义模块后，要创建实例，格式应该为，变量 = 模块名.类名()
#m = m1.mousefunction()
#导入方式2，直接可以读取类名，通过类名创建实例
mf = mousefunction()

# 发送粘贴
# win32gui.PostMessage(hwnd,win32con.WM_PASTE, 0, 0)

xy =  mf.cursor_point()
print(xy[0],xy[1])

"""
#画斜线
mf.bkg_mouse_left_down(hwnd,x,y)
for i in range(1,100):
    mf.bkg_mouse_move(hwnd,x+i,y+i)
    time.sleep(0.05)
mf.bkg_mouse_left_up(hwnd,x,y)
"""

#画圆
r=60
x0=470 #圆心位置x
y0=420 #圆心位置y
x=0
y=0
n=0
while n < 3.1415926*2:
    x=x0+r*math.cos(n)
    y=y0-r*math.sin(n)
    if n==0:
        mf.mouse_left_down(int(x),int(y))
    mf.mouse_move(int(x),int(y))
    time.sleep(0.03)
    n=n+0.03
mf.mouse_left_up(int(x),int(y))


"""
Sub 画圆()
    r=300:x0=512:y0=384:x=0:y=0:n=0
    While n<3.1415926*2
        x=x0+r*cos(n)
        y=y0-r*sin(n)
        MoveTo x,y
        Delay 20
        n=n+0.03
    Wend
End Sub
"""




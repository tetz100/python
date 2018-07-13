#-------------------------------------------------------------------------------
# Name:        image
# Purpose:     用于图片的处理
#
# Author:      GhostAemi
#
# Created:     05-07-2018
# Copyright:   (c) GhostAemi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from PIL import Image
import operator
import win32api
import win32con
import win32gui
import time
import random
import math
import configparser
import os
import sys

import mouse

class image:

    def printImgLine():
        flag = 0
        #绘制图像 ，range(开始/起始点,结束/结束点,步长)
        for i in range(1,height,1):
            for j in range(1,width,1):
                x = j
                y = i
                if x == 1:
                    None
                else:
                    # 如果鼠标按下移动到了图片最右边，则松开鼠标
                    if x == (width - 1) :
                        mf.bkg_mouse_left_up(hwnd,int(swx) + x - 1,int(swy) + y - 1)
                        flag = 0
                    elif im.getpixel((x,y)) == 0:
                        #如果第2个点是黑色并且，第1个点也是黑色就按下鼠标
                        if x == 2 and im.getpixel((x - 1,y)) == 0:
                            mf.bkg_mouse_left_down(hwnd,int(swx) + x,int(swy) + y)
                            flag = 1
                        else :
                            if flag == 0 :
                                #判断上一个像素是否是白色，是就按下鼠标，不是就移动鼠标
                                if im.getpixel((x - 1,y)) == 255 :
                                    mf.bkg_mouse_left_down(hwnd,int(swx) + x,int(swy) + y)
                                    flag = 1
                                else:
                                    #如果从黑色到了白色就移动鼠标
                                    if im.getpixel((x + 1,y)) == 255 :
                                        mf.bkg_mouse_move(hwnd,int(swx) + x,int(swy) + y)
                            else :
                                #如果从黑色到了白色就移动鼠标
                                if im.getpixel((x + 1,y)) == 255 :
                                    mf.bkg_mouse_move(hwnd,int(swx) + x,int(swy) + y)
                    elif flag == 1 :
                        mf.bkg_mouse_left_up(hwnd,int(swx) + x - 1,int(swy) + y - 1)
                        flag = 0

    def printImgPoint():
        #绘制图像 ，range(开始/起始点,结束/结束点,步长)
        for i in range(0,height,1):
            for j in range(0,width,1):
                x = j
                y = i
                RGB = im.getpixel((x,y))
                if RGB == 0 :
                    #如果该点是黑色，则绘制
                    #ms.mouse_left_click(x,y)
                    mf.bkg_mouse_left_click(hwnd,int(swx) + x,int(swy) + y)

    def printYuan():
        #画圆
        r=120
        x0=wx #圆心位置x
        y0=wy #圆心位置y
        x=0
        y=0
        n=0
        while n < 3.1415926*2:
            x=x0+r*math.cos(n)
            y=y0-r*math.sin(n)
            if n==0:
                mf.bkg_mouse_left_down(hwnd,int(x),int(y))
            mf.bkg_mouse_move(hwnd,int(x),int(y))
            time.sleep(0.03)
            n=n+0.03
        mf.bkg_mouse_left_up(hwnd,int(x),int(y))

    def appMain():
        #打开图片
        im=Image.open(imgPath)

        #得到图片的大小
        imgSize = im.size
        width = imgSize[0]
        height = imgSize[1]

        #将图片转换成黑白
        im = im.convert('1')
        #保存图片
        #im.save(r"D:\pyFiles\file\result3.png")

        #找到窗口的坐标
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        #如果判断获取窗口数据时，窗口是最小化就停止程序、
        if left < 0 and top < 0 and right < 0 and bottom < 0 :
            print("窗口被最小化，停止程序，按任意键关闭")
            ex = input()
            sys.exit()
        #窗口的中点x
        wx = (right - left) / 2
        #窗口的中点y
        wy = (bottom - top) / 2
        #减去图片的中点的x和y
        swx = wx - (width / 2)
        swy = wy - (height / 2)
        print("句柄：",hwnd)
        print("窗口数据：",left, top, right, bottom)

        if printMethod == '1' :
           image.printImgLine()
        elif printMethod == '2' :
           image.printImgPoint()
        elif printMethod == '3' :
           image.printYuan()
        elif printMethod == '4' :
           image.printImgLine()
           image.printYuan()
        elif printMethod == '5' :
            image.printImgPoint()
            image.printYuan()
        else:
            print("输入错误，重新开始")

#创建配置文件
def creatConfig():
    #写入配置文件
    #添加值
    conf.set('config','#注意：配置完后一定要保存再继续','')
    conf.set('config','#是否永久保存该配置内容(yes/no)','')
    conf.set('config','saveTheConfig','no')
    conf.set('config','#设置窗口类名和窗口标题：','')
    conf.set('config','windowClassName','')
    conf.set('config','windowTitle','')
    conf.set('config','#如果不设置窗口类名和窗口标题，请手动设置句柄值，优先使用此项','')
    conf.set('config','hwnd','')
    conf.set('config','#图片路径，例：D:/pyFiles/file','')
    conf.set('config','imgPath','')
    conf.set('config','#设置绘制速度（0 到 1000，0最快）','')
    conf.set('config','timeOut','0')
    conf.set('config','#DEBUG(on表示不开启，yes表示开启)','')
    conf.set('config','debug','no')
    conf.set('config','是否保存转换的图片(yes/on)','')
    conf.set('config','saveImg','no')
    conf.set('config','绘制位置(基于句柄窗口的客户区,默认窗口中间，单位像素)','')
    conf.set('config','x','')
    conf.set('config','y','')
    #写入文件
    with open('config.ini','w') as fw:
        conf.write(fw)

    #打开配置文件
    time.sleep(1)
    os.popen('C:/Windows/notepad.exe config.ini')

#加载现有配置文件
conf = configparser.ConfigParser()

#先判断是否存在配置文件
if os.path.exists("config.ini"):
    #存在就读取配置文件
    conf.read("config.ini")
    saveTheConfig = conf.get('config','saveTheConfig')
    #判断是否是永久保存的配置文件 ,不是就重新创建
    if saveTheConfig != "yes" :
        creatConfig()
else :
    #添加section
    conf.add_section('config')
    #不存在就创建
    creatConfig()

print("请先修改配置文件！！")
questSave = input("确定配置完成并且正确而且已保存？输入其他内容打开配置文件，直接回车继续")
if questSave != "":
    os.popen('C:/Windows/notepad.exe config.ini')
    input("请再次确认配置无误，回车继续")

reFlag = 1
while reFlag:
    #每次循环都要求读取配置文件
    conf.read("config.ini")
    windowClassName = conf.get('config','windowClassName')
    windowTitle = conf.get('config','windowTitle')
    hwnd = conf.get('config','hwnd')
    imgIndexPath = conf.get('config','imgPath')
    timeOut = conf.get('config','timeOut')
    debug = conf.get('config','debug')
    saveImg = conf.get('config','saveImg')
    printX = conf.get('config','x')
    printY = conf.get('config','y')

    print(windowClassName,windowTitle,hwnd,imgIndexPath,timeOut,debug,saveImg,printX,printY)

    #创建鼠标操作对象，参数(延迟毫秒数，是否打印)
    if int(timeOut) > 0 and debug == 'no' :
        mf = mouse.mousefunction(int(timeOut))
    elif int(timeOut) == 0 and debug == 'no':
        mf = mouse.mousefunction(0)
    elif int(timeOut) > 0 and debug == 'yes' :
        mf = mouse.mousefunction(int(timeOut),1)
    elif int(timeOut) == 0 and debug == 'yes' :
        mf = mouse.mousefunction(0,1)
    else :
        input('错误的配置数据！')
        os.popen('C:/Windows/notepad.exe config.ini')
        sys.exit()

    #获取窗口句柄
    if hwnd == "" :
        if windowClassName != "" and windowTitle != "" :
            #得到窗口句柄对象
            handle = win32gui.FindWindow(windowClassName, windowTitle)
            hwnd = handle.__int__()
        else :
            input("句柄参数不正确，请检查配置")
            os.popen('C:/Windows/notepad.exe config.ini')
            sys.exit()
    else :
        hwnd = int(hwnd)
    ###################################
    #设置图片
    print(r"设置图片，输入图片名和后缀（图片请放在",imgIndexPath,"目录下），否则直接回车：随机")
    inputImg = input()
    if inputImg == "" :
        #读取指定文件夹下的所有文件
        fileArr = []
        imgArr = []
        for root, dirs, files in os.walk(imgIndexPath):
            fileArr = files
        if len(fileArr) == 0 :
            input("该目录下没有图片，请放入图片")
            sys.exit()
        else :
            for i in range(len(fileArr)):
                item = fileArr[i].split('.')
                if item[1] == "jpg" or item[1] == "png" or item[1] == "bmp" or item[1] == "png" or item[1] == "gif":
                    imgArr.append(fileArr[i])
        if len(imgArr) == 0 :
            input("该目录下没有图片，请放入图片")
            sys.exit()

        #图片数组随机
        imgName = random.choice(imgArr)
        #判断文件后缀
        imgPath = imgIndexPath + '/' + imgName
        print("得到图片:",imgPath)

    else :
        imgPath = imgIndexPath + '/' + inputImg
        #判断文件是否存在
        if not os.path.exists(imgPath):
            input("文件不存在，重新选择"+imgPath)
            continue
        print("得到图片:",imgPath)

    #打开图片
    im=Image.open(imgPath)

    #得到图片的大小
    imgSize = im.size
    width = imgSize[0]
    height = imgSize[1]

    print("图片尺寸",width,"*",height)

    #将图片转换成黑白
    im = im.convert('1')
    #保存图片
    if saveImg == "yes" :
        im.save(imgIndexPath + "/result.png")


    print("得到句柄：",hwnd)
    #判断窗口是否存在
    ###找不到方法
     #找到窗口的坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    #如果判断获取窗口数据时，窗口是最小化就停止程序、
    if left < 0 and top < 0 and right < 0 and bottom < 0 :
        input("窗口被最小化，将重新开始，回车继续")
        continue
    #窗口的中点x
    wx = (right - left) / 2
    #窗口的中点y
    wy = (bottom - top) / 2
    #位置坐标，减去图片的中点的x和y
    swx = wx - (width / 2)
    swy = wy - (height / 2)
    print("窗口数据：",left, top, right, bottom)

    #是否设置绘图位置坐标
    if printX != "" and printY != "" :
        swx = int(printX)
        swy = int(printY)

    #选择绘图方式
    print("请选择使用那种方式画图（1，画线方式；2，画点方式；3，画圆；4，画线+画圆；5，画点+画圆），直接回车：重新开始")
    printMethod =  input()

    #开始绘制
    if printMethod == '1' :
        image.printImgLine()
    elif printMethod == '2' :
        image.printImgPoint()
    elif printMethod == '3' :
        image.printYuan()
    elif printMethod == '4' :
        image.printImgLine()
        image.printYuan()
    elif printMethod == '5' :
        image.printImgPoint()
        image.printYuan()
    else:
        print("输入错误，重新开始")

    print("运行结束，是否再来一次，直接回车:是")
    reStart = input()
    if reStart != "" :
        reFlag = 0




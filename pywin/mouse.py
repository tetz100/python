#-------------------------------------------------------------------------------
# Name:        mousefunction
# Purpose:     这是鼠标操作封装
#
# Author:      Administrator
#
# Created:
# Copyright:   (c) Administrator
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from ctypes import *
import win32api
import win32con
import win32gui
import time
import os

#操作控制接口封装
class mousefunction:

    #初始化
    def __init__(self,timeOut = None,printFlag = None):
        """
        初始化鼠标控制接口
        :param timeOut: 设置全局鼠标操作延迟，默认50毫秒，单位毫秒
        :param printFlag: 设置是否打印执行内容，默认0，不打印
    	"""
        if timeOut is not None :
            self.timeOut = timeOut / 1000
        else:
            self.timeOut = 0.05
        if printFlag is not None :
            self.printFlag = printFlag
        else:
            self.printFlag = 0


    #获取当前鼠标位置
    def cursor_point(self):
    	"""
    	 获取当前鼠标位置
    	"""
    	pos = win32api.GetCursorPos()
    	if self.printFlag :
    	   print("[mousefunction]获取当前鼠标位置：",int(pos[0]), int(pos[1]))
    	return int(pos[0]), int(pos[1])


    #移动鼠标位置
    def mouse_move(self,new_x, new_y):
    	"""
        移动鼠标位置，如果没指定坐标，则获取当前鼠标的坐标
        :param new_x: 新移动的坐标x轴坐标
        :param new_y: 新移动的坐标y轴坐标
    	"""
    	if new_y is not None and new_x is not None:
    		point = (new_x, new_y)
    		win32api.SetCursorPos(point)
    		self.x = new_x
    		self.y = new_y
    	if self.printFlag :
    	   print("[mousefunction]鼠标移动，坐标：",new_x, new_y)

    #鼠标左击事件
    def mouse_left_click(self,new_x=None, new_y=None, times=1):
    	"""
    	鼠标左击事件
    	:param new_x: 新移动的坐标x轴坐标
    	:param new_y: 新移动的坐标y轴坐标1506240215
    	:param times: 点击次数
    	"""
    	conut = times
    	self.mouse_move(new_x, new_y)
    	time.sleep(0.005)
    	while times:
    		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    		times -= 1
    	if self.printFlag :
    	   print("[mousefunction]鼠标左击",conut,"次，","坐标：",new_x, new_y)

    #鼠标右击事件
    def mouse_right_click(self,new_x=None, new_y=None):
    	"""
    	鼠标右击事件
    	:param new_x: 新移动的坐标x轴坐标
    	:param new_y: 新移动的坐标y轴坐标
    	"""
    	self.mouse_move(new_x, new_y)
    	time.sleep(self.timeOut)
    	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
    	if self.printFlag :
    	   print("[mousefunction]鼠标右击1次，坐标：",new_x, new_y)



    #鼠标左键按下事件
    def mouse_left_down(self,new_x=None,new_y=None):
        """
    	鼠标左键按下事件
    	:param new_x: 新移动的坐标x轴坐标
    	:param new_y: 新移动的坐标y轴坐标
    	"""
        self.mouse_move(new_x,new_y)
        time.sleep(self.timeOut)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        if self.printFlag :
            print("[mousefunction]鼠标左键按下,坐标：",new_x,new_y)

    #鼠标左键松开事件
    def mouse_left_up(self,new_x=None,new_y=None):
        """
        鼠标左键松开事件
        :param new_x: 新移动的坐标x轴坐标
        :param new_y: 新移动的坐标y轴坐标
        """
        self.mouse_move(new_x,new_y)
        time.sleep(self.timeOut)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        if self.printFlag :
            print("[mousefunction]鼠标左键松开,坐标：",new_x,new_y)

    #鼠标右键按下事件
    def mouse_right_down(self,new_x=None,new_y=None):
        """
        鼠标右键按下事件
        :param new_x: 新移动的坐标x轴坐标
        :param new_y: 新移动的坐标y轴坐标
        """
        self.mouse_move(new_x,new_y)
        time.sleep(self.timeOut)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        if self.printFlag :
            print("[mousefunction]鼠标右键按下,坐标：",new_x,new_y)

    #鼠标右键松开事件
    def mouse_right_up(self,new_x=None,new_y=None):
        """
        鼠标右键松开事件
        :param new_x: 新移动的坐标x轴坐标
        :param new_y: 新移动的坐标y轴坐标
        """
        self.mouse_move(new_x,new_y)
        time.sleep(self.timeOut)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        if self.printFlag :
            print("[mousefunction]鼠标右键松开,坐标：",new_x,new_y)

    #鼠标后台
    #发送移动鼠标位置事件
    def bkg_mouse_move(self,hwnd,new_x,new_y):
        if new_y is not None and new_x is not None:
            """
            发送移动鼠标位置，如果没指定坐标，则获取当前鼠标的坐标
            :param hwnd: 窗口十进制句柄
            :param new_x: 新移动的坐标x轴坐标
            :param new_y: 新移动的坐标y轴坐标
            """
            #坐标点转换
            tmp = win32api.MAKELONG(new_x, new_y)
            # 发送激活窗口状态
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        	# 发送鼠标移动
            win32api.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, tmp)
            self.x = new_x
            self.y = new_y
        else:
            xy = self.cursor_point()
            self.x = xy[0]
            self.y = xy[1]
        if self.printFlag :
            print("[mousefunction]发送鼠标移动事件，坐标：",new_x, new_y)

    #发送鼠标左击事件
    def bkg_mouse_left_click(self,hwnd,new_x = None,new_y = None,times = 1):
        """
        发送鼠标左击事件，使用后台鼠标操作必须指定坐标
        :param hwnd: 窗口十进制句柄
        :param new_x: 新移动的坐标x轴坐标
        :param new_y: 新移动的坐标y轴坐标
        :param times: 鼠标点击次数
        """
        conut = times
        self.bkg_mouse_move(hwnd,new_x, new_y)
        time.sleep(self.timeOut)
        while times:
            #坐标点转换
            tmp = win32api.MAKELONG(self.x, self.y)
            # 发送激活窗口状态
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
            # 发送按下鼠标左键
            win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
            # 发送松开鼠标左键
            win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
            times -= 1
        if self.printFlag :
            print("[mousefunction]发送鼠标左击",conut,"次事件，坐标：",new_x, new_y)

    #发送鼠标右击事件
    def bkg_mouse_right_click(self,hwnd,new_x, new_y):
        """
        发送鼠标右击事件，使用后台鼠标操作必须指定坐标
        :param hwnd: 窗口十进制句柄
        :param new_x: 新移动的坐标x轴坐标
        :param new_y: 新移动的坐标y轴坐标
        """
        self.bkg_mouse_move(hwnd,new_x, new_y)
        time.sleep(self.timeOut)
         #坐标点转换
        tmp = win32api.MAKELONG(self.x, self.y)
        # 发送激活窗口状态
        win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        # 发送按下鼠标右键
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, tmp)
        # 发送松开鼠标右键
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, tmp)
        if self.printFlag :
            print("[mousefunction]发送鼠标右击事件，坐标：",new_x, new_y)

    #发送鼠标左键按下事件
    def bkg_mouse_left_down(self,hwnd,new_x,new_y):
        """
        发送鼠标左键按下事件，使用后台鼠标操作必须指定坐标
        :param hwnd: 窗口十进制句柄
        :param new_x: 新移动的坐标x轴坐标
        :param new_y: 新移动的坐标y轴坐标
        """
        self.bkg_mouse_move(hwnd,new_x, new_y)
        time.sleep(self.timeOut)
         #坐标点转换
        tmp = win32api.MAKELONG(self.x, self.y)
        # 发送激活窗口状态
        win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        # 发送按下鼠标左键
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
        if self.printFlag :
            print("[mousefunction]发送鼠标左键按下事件，坐标：",new_x, new_y)

    #发送鼠标左键松开事件
    def bkg_mouse_left_up(self,hwnd,new_x,new_y):
        """
        发送鼠标左键松开事件，使用后台鼠标操作必须指定坐标
        :param hwnd: 窗口十进制句柄
        :param new_x: 新移动的坐标x轴坐标
        :param new_y: 新移动的坐标y轴坐标
        """
        self.bkg_mouse_move(hwnd,new_x, new_y)
        time.sleep(self.timeOut)
         #坐标点转换
        tmp = win32api.MAKELONG(self.x, self.y)
        # 发送激活窗口状态
        win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        # 发送松开鼠标左键
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
        if self.printFlag :
            print("[mousefunction]发送鼠标左键松开事件，坐标：",new_x, new_y)

    #发送鼠标右键按下事件
    def bkg_mouse_right_down(self,hwnd,new_x,new_y):
        """
        发送鼠标右键按下事件，使用后台鼠标操作必须指定坐标
        :param hwnd: 窗口十进制句柄
        :param new_x: 新移动的坐标x轴坐标
        :param new_y: 新移动的坐标y轴坐标
        """
        self.bkg_mouse_move(hwnd,new_x, new_y)
        time.sleep(self.timeOut)
         #坐标点转换
        tmp = win32api.MAKELONG(self.x, self.y)
        # 发送激活窗口状态
        win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        # 发送按下鼠标右键
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, tmp)
        if self.printFlag :
            print("[mousefunction]发送鼠标右键按下事件，坐标：",new_x, new_y)

    #发送鼠标右键松开事件
    def bkg_mouse_right_up(self,hwnd,new_x,new_y):
        """
        发送鼠标右键松开事件，使用后台鼠标操作必须指定坐标
        :param hwnd: 窗口十进制句柄
        :param new_x: 新移动的坐标x轴坐标
        :param new_y: 新移动的坐标y轴坐标
        """
        self.bkg_mouse_move(hwnd,new_x, new_y)
        time.sleep(self.timeOut)
         #坐标点转换
        tmp = win32api.MAKELONG(self.x, self.y)
        # 发送激活窗口状态
        win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        # 发送松开鼠标右键
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, tmp)
        if self.printFlag :
            print("[mousefunction]发送鼠标右键松开事件，坐标：",new_x, new_y)







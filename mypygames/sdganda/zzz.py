from PIL import ImageDraw,ImageGrab
import PIL.Image
import win32gui,win32con,win32api
import cv2
import numpy as np
import time
from ctypes import *
from tkinter import *
import tkinter as tk
import threading

gdi32 = windll.gdi32
user32 = windll.user32
hdc = user32.GetDC(None)
classname = "Qt5QWindowIcon"
titlename = "逍遥模拟器"
hwnd = win32gui.FindWindow(classname, titlename)
# 获取窗口左上角和右下角坐标
win32gui.SetForegroundWindow(hwnd)
global left, top, right, bottom,res
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(left, top, right, bottom)
time.sleep(1)

def mouse_click(x, y):    # 鼠标左键点击屏幕上的坐标(x, y)
    x=10,y=10
    win32api.SetCursorPos((x, y))    # 鼠标定位到坐标(x, y)
    # 注意：不同的屏幕分辨率会影响到鼠标的定位，有需求的请用百分比换算
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)    # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 鼠标左键弹起

def screenshot():
    bbox = (left, top, right, bottom)
    im = ImageGrab.grab(bbox)
    im.save('sc.png')

def dingwei(x, y):
    img = cv2.imread('sc.png', 0)
    template = cv2.imread(x, 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = y
    gps = []
    loc = np.where(res >= threshold)  # 匹配程度大于%95的坐标y,x
    for pt in zip(*loc[::-1]):       # *号表示可选参数
        gps.append(pt)
    return gps

def circle(m, n, img):
    a = ImageDraw.Draw(img)
    a.text((m, n), "target", fill=(255, 0, 0), font=None)
    a.rectangle((m, n, m + 325, n + 120), outline="red")
    return img

def tupo():
    res = dingwei('0.png', 0.92)
    re = res[0]
    time.sleep(1)
    mouse_click(left + re[0] + 10, top + re[1] + 10)
    time.sleep(3)
    mouse_click(left + re[0] + 245, top + re[1] + 245)
    time.sleep(30)

    c = gdi32.GetPixel(hdc, left + 985, top + 554)
    d = gdi32.GetPixel(hdc, left + 1109, top + 554)

    while(c != d or (c!=6271732 and c!=10528944)):
        mouse_click(left + 113, top + 313)
        time.sleep(7)
        c = gdi32.GetPixel(hdc, left + 985, top + 554)
        d = gdi32.GetPixel(hdc, left + 1109, top + 554)

    print('继续突破')
    mouse_click(left + 113, top + 313)
    time.sleep(6)

def draw(x, y):
    res = dingwei(x, y)
    img = PIL.Image.open(u'sc.png')
    for i in range(len(res)):
        re = res[i]
        img = circle(re[0], re[1], img)
    return res

def num():
    if len(res) != 0:
        o = [res[0]]
        for i in range(len(res) - 1):
            a = abs(res[i + 1][0] - res[i][0]) + abs(res[i + 1][1] - res[i][1])
            if a >= 100:
                o.append(res[i + 1])
        print(o)
        return(len(o))
    else:
        return(0)

def start():
    global left, top, right, bottom,res
    time.sleep(1)
    while (on_hit == True):
        screenshot()
        time.sleep(5)
        res = draw('0.png', 0.92)#0.png为待突破的结界样本图片
        nu1 = num()
        res = draw('1.png', 0.90)#1.png为已突破的结界样本图片
        nu2 = num()
        print("待突破结界:",nu1,"已突破结界:",nu2)
        if nu1 != 0 and nu2 < 3:
            tupo()
        elif nu1 != 0 and nu2 >= 3:
            while(gdi32.GetPixel(hdc, left + 985, top + 554) == 10528944):
                time.sleep(5)
            mouse_click(left + 1109, top + 571)
            time.sleep(1)
            mouse_click(left + 758, top + 447)
            time.sleep(3)
        elif nu1 == 0:
            mouse_click(left + 1109, top + 571)
            time.sleep(1)
            mouse_click(left + 758, top + 447)
            time.sleep(3)
    print("结束") 

def xuan():
    while (on_hit == True):
        e = gdi32.GetPixel(hdc, left + 514, top + 170)
        f = gdi32.GetPixel(hdc, left + 728, top + 167)

        if (e != f or e != 7967411):
            time.sleep(1)
            e = gdi32.GetPixel(hdc, left + 514, top + 170)
            f = gdi32.GetPixel(hdc, left + 728, top + 167)
        else:
            mouse_click(left + 859, top + 447)

window = Tk()
window.title('公众号调和制作')
window.geometry('480x150')
logo = PhotoImage(file="t.png")#t.png为脚本上的装饰图片
w1 = Label(window, image=logo).pack(side="top")
explanation = """本软件仅用于测试，说明：
仅适用于电脑分辨率1920*1080，逍遥模拟器1080*720，
首先打开个人结界突破主页面，锁定好阵容，点击开始→"""

tk.Label(window,text=explanation,justify=LEFT).place(x=10,y=85,anchor='nw')

var = tk.StringVar()
on_hit = False
var.set('开始')

def hit():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('结束')
    else:
        on_hit = False
        var.set('开始')

def duo():
    threads = []
    threads.append(threading.Thread(target=hit))
    threads.append(threading.Thread(target=start))
    threads.append(threading.Thread(target=xuan))
    for t in threads:
        t.start()

b = tk.Button(window, textvariable=var, command=duo, width=15, height=2,).place(x=340,y=90,anchor='nw')

window.mainloop()
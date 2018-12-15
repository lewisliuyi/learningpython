import pyautogui
import random
import time
import win32gui,win32con,win32api

def getWindows():
    titlename = "Gundam Online"
    hwnd = win32gui.FindWindow(0, titlename)
    win32gui.SetForegroundWindow(hwnd)
    return None


def getPosition(name, regionscale):
    pngAdress = name + '.png'
    x = 0
    i = 1
    while x == 0:
        print('第%d次定位中' % i)
        locate = pyautogui.locateOnScreen(
            pngAdress, region=regionscale, grayscale=True)
        if locate == None:
            print('没有找到%s,请检查' % name)
            i = i + 1
            time.sleep(1)
        else:
            x, y = pyautogui.center(locate)
            print('%s 已经定位成功' % name)
    return [x, y]


def clickPicture(locate, times, clickButton='left'):
    x, y = locate[0], locate[1]
    pyautogui.click(
        x=x,
        y=y,
        clicks=times,
        button=clickButton,
        interval=2)
    print('%s点击%d次，已经完成' % (clickButton,times))


def attack():
    #识别敌人并且发起进攻
    pyautogui.mouseDown(button='right')
    pyautogui.press('2', presses=2)
    movetimes = random.randint(5, 8)
    randomkeys = ['w', 's', 'd', 'a']
    for i in range(movetimes):
        randomkey = randomkeys[random.randint(0, 3)]
        pyautogui.keyDown(randomkey)
        pyautogui.moveRel(xOffset=random.randint(180,220), duration=3)
        clickTimes = random.randint(3, 6)
        pyautogui.click(clicks=clickTimes, interval=random.uniform(2, 5))
        pyautogui.keyUp(randomkey)
    pyautogui.mouseUp(button='right')


def battary():
    while x == 0:
        print('第%d次定位电池中' % i)
        clickPicture()
        if locate == None:
            print('没有找到机体,请检查是否在房间')
            i = i + 1
        else:
            x, y = pyautogui.center(locate)
            pyautogui.click(x=x, y=y, button='right', interval=random.random())
            pyautogui.moveRel(
                xOffset == 10, yOffset == 10, duration=random.random())
            pyautogui.click()
            print('电池已经充电')
            x = 1


def sougouKa():
    pyautogui.press('enter')
    time.sleep(random.uniform(0, 2))
    pyautogui.hotkey('ctrl', 'shift', 'm', interval=1)
    pyautogui.press(['a', 'z'], interval=random.random())
    if getPosition('sougouSuccess',allRegions['sougouSuccess']) !=None:
        print('卡成功')
    time.sleep(270)
    pyautogui.click(
        x=random.randint(800, 1200), clicks=2, interval=random.random)
    pyautogui.press('a')
    time.sleep(random.uniform(1, 3))
    pyautogui.press(['ctrl', 'tab'], interval=random.random())


def gameOver():
    overPNG = u'结束界面.png'


def returnToGame():
    pass


def main():
    runtimes = int(input('请输入循环的次数'))
    f5x, f5y = getPosition('f5', allRegions['f5'])
    smallf5 = (f5x - 100, f5y - 100, f5x + 70, f5y + 70)
    titlename = "Gundam Online"
    hwnd = win32gui.FindWindow(0, titlename)
    win32gui.SetForegroundWindow(hwnd)
    for i in range(runtimes):
        if i % 10 != 0:  #判断是否要充电
            battary()
        clickPicture(
            getPosition('f5', allRegions['f5']), times=3)  #判断是否在大厅，定位F5,并开始
        pyautogui.press('f5')
        pyautogui.press('f5')
        time.sleep(1)
        pyautogui.press('f5')
        time.sleep(8)
        #getPosition('start',allRegions['start'])
        time.sleep(5)
        attack()
        sougouKa()
        pyautogui.click(x=1000,y=500,clicks=random.randint(8,13),interval=random.uniform(1,2))


allRegions = {'f5': (600, 300, 1400, 1000),'start':(20,20,600,400),'sougouSuccess':(600,300,1500,700)}

if __name__ == "__main__":
    main()

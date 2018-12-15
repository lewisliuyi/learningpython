import win32api
import time
import win32con
def move_click(x, y, t=0):  # 移动鼠标并点击左键
    win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                         win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
    if t == 0:
        time.sleep(random.random()*2+1)  # sleep一下
    else:
        time.sleep(t)
    return 0

# 测试
move_click(30, 30)

#当然，再后续操作中你可能需要获取屏幕分辨率，我只打算让脚本能在自己电脑上跑就满足了，所以没有实现适配不同分辨率

def resolution():  # 获取屏幕分辨率
    return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

#值得注意的是，一定要在管理员权限下的cmd中运行，否则点击无效

#这个时候，你已经可以写个while循环，不停地点击屏幕上不同的几个点了，最基础的挂机脚本就实现了

#使用PIL识别图像
#我们肯定不满足于机械式的连续点击，万一被封号呢… 
#所以需要识别图像，再进行点击 
#首先，就需要定位到阴阳师的窗口

import win32gui
def get_window_info():  # 获取阴阳师窗口信息
    wdname = u'阴阳师-网易游戏'
    handle = win32gui.FindWindow(0, wdname)  # 获取窗口句柄
    if handle == 0:
        # text.insert('end', '提示：请打开sd敢达\n')
        # text.see('end')  # 自动显示底部
        return None
    else:
        return win32gui.GetWindowRect(handle)


#get_window_info()函数返回阴阳师窗口信息(x1, y1, x2, y2)，(x1, y1)是窗口左上角的坐标，(x2, y2)是窗口右下角的坐标，代码中的text可以暂时忽略，这在后续GUI界面中用于输出提示信息。 
#下面使用PIL获取游戏截图

def get_posx(x, window_size):  # 返回x相对坐标
    return (window_size[2] - window_size[0]) * x / 870


def get_posy(y, window_size):  # 返回y相对坐标
    return (window_size[3] - window_size[1]) * y / 520

topx, topy = window_size[0], window_size[1]
img_ready = ImageGrab.grab((topx + get_posx(500, window_size), topy + get_posy(480, window_size),
                            topx + get_posx(540, window_size), topy + get_posy(500, window_size)))
# 查看图片
im_ready.show()

#考虑到窗口大小不同，位置会有所偏移，这里使用屏幕上点的相对位置 
#获取到关键位置的截图之后，计算图片的hash值

def get_hash(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
    avg = sum(list(img.getdata())) / 256  # 计算像素平均值
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # 每个像素进行比对,大于avg为1,反之为0
    return ''.join(map(lambda j: '%x' % int(s[j:j+4], 2), range(0, 256, 4)))

#将关键位置截图的hash值保存下来，下次脚本运行时，将截图hash值与原始hash值进行比对，判断是否相似。 
#这里使用汉明距离进行计算，比较hash值中相同位置上不同元素的个数

def hamming(hash1, hash2, n=20):
    b = False
    assert len(hash1) == len(hash2)
    if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
        b = True
    return b

#准备工作做完了，下面就可以开心刷御灵了

def yu_ling(window_size):
    global is_start
    topx, topy = window_size[0], window_size[1]
    state = []

    while is_start:
        # print 'start'
        # text.insert('end', 'start')
        time.sleep(0.5)
        img_ready = ImageGrab.grab((topx + get_posx(750, window_size), topy + get_posy(465, window_size),
                                    topx + get_posx(840, window_size), topy + get_posy(500, window_size)))
        if hamming(get_hash(img_ready), ready_hash, 10):
            state.append(0)
            move_click(topx + get_posx(740, window_size), topy + get_posy(380, window_size))
            text.insert('end', strftime('%H:%M:%S', localtime()) + ' 点击准备\n')
            text.see('end')  # 自动显示底部
            time.sleep(15)
            continue

        img_success = ImageGrab.grab((topx + get_posx(400, window_size), topy + get_posy(320, window_size),
                                      topx + get_posx(470, window_size), topy + get_posy(400, window_size)))
        if hamming(get_hash(img_success), success_hash):
            time.sleep(2)
            state.append(1)
            text.insert('end', strftime('%H:%M:%S', localtime()) + ' 成功%d次\n' % state.count(1))
            text.see('end')  # 自动显示底部
            move_click(topx + get_posx(730, window_size), topy + get_posy(380, window_size))
            continue

        img_fail = ImageGrab.grab((topx + get_posx(560, window_size), topy + get_posy(340, window_size),
                                   topx + get_posx(610, window_size), topy + get_posy(390, window_size)))
        if hamming(get_hash(img_fail), fail_hash):
            time.sleep(2)
            state.append(2)
            text.insert('end', strftime('%H:%M:%S', localtime()) + ' 失败%d次\n' % state.count(2))
            text.see('end')  # 自动显示底部
            move_click(topx + get_posx(720, window_size), topy + get_posy(380, window_size))
            continue

        img_attack = ImageGrab.grab((topx + get_posx(615, window_size), topy + get_posy(350, window_size),
                                     topx + get_posx(675, window_size), topy + get_posy(375, window_size)))
        if hamming(get_hash(img_attack), yu_attack_hash):
            move_click(topx + get_posx(670, window_size), topy + get_posy(365, window_size))
            text.insert('end', strftime('%H:%M:%S', localtime()) + ' 点击进攻\n')
            text.see('end')  # 自动显示底部
            state.append(3)
            if state[-6:] == [3]*6:
                text.insert('end', strftime('%H:%M:%S', localtime()) + ' 痴汉券可能不够了\n')
                text.see('end')  # 自动显示底部
                click()
                break
            continue

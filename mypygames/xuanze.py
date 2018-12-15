import random
choice = []
signle = []
global itemsNumber
itemsNumber = 0
b = 0
i = 0
print("请输入纠结的选择,输入'q'停止输入")
while True:
    # 添加输入的内容
    choice.append(str(input("请输入第%d种选择：" % (itemsNumber + 1))))
    if choice[itemsNumber] == 'q':
        for i in range(itemsNumber):
            signle.append(0)
            i += 1
        break
    itemsNumber += 1
alltimes = int(input("请输入想要随机的次数："))
while b < alltimes:
    answer = random.randint(0, itemsNumber - 1)
    print("第%d次结果是:%s" % (b + 1, choice[answer]))
    b = b + 1
    signle[answer] += 1
print("最终统计的结果是：")
for i in range(itemsNumber):
    print("\t%s的次数是：%d" % (choice[i], signle[i]))
print("现在你有选择了吗(*^_^*)")

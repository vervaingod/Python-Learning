"""
输出乘法口诀表

"""
# 定义阿拉伯数字和汉字之间转换的字典
numDict = {1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "七", 8: "八", 9: "九"}


# 将两位数字转化为对应的汉字
def changeNum(x):
    a = int(x / 10)  # 十位
    b = x % 10  # 个位
    if a > 0 and b > 0:
        return str(numDict.get(a)) + str(numDict.get(b))
    elif a > 0 and b == 0:
        return numDict.get(a)
    elif a == 0 and b > 0:
        return numDict.get(b)


# 计算数字乘法口诀表
for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print("%s*%s=%s" % (numDict.get(i), numDict.get(j), changeNum(i * j)), end=" ")
    print("")

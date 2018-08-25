"""
1. 实现摄氏（C）和华氏（F）的双向转换，实现英寸（in）和厘米（cm）的双向转换，实现美元（$）和人民币（￥）的双向转换（以当日汇率为准）。

2. 运行后可多次输入并转换，添加退出条件判断（如：输入q退出
"""


# 转换温度方法
def changeTem(x):
    try:
        type = x[-1]  # 截取最后一位单位
        if (type == "C"):
            celsius = float(x[:-1])
            fahrenheit = (celsius * 2.0) + 32  # 计算华氏温度
            print("Tf=(" + str(celsius) + ")*2.0+32=" + str(fahrenheit) + "F")
        elif (type == "F"):
            fahrenheit = float(x[:-1])
            celsius = (fahrenheit - 32) / 2  # 计算摄氏温度
            print("Tc=(" + str(fahrenheit) + "-32)/2=" + str(celsius) + "C")
        else:
            print("输入的数据有误，请确保最后一位是T或F")
    except:
        print("输入的数据有误，请检查确保除最后一位外是数字")  # 异常处理


# 长度转换
def changeLon(x):
    try:
        type = x[-2:]  # 截取后两位
        if (type == "in"):
            longIN = float(x[:-2])
            longCM = longIN * 2.54
            print("Lcm=" + str(longIN) + "*2.54=" + str(longCM) + "cm")
        elif (type == "cm"):
            longCM = float(x[:-2])
            longIN = longCM / 2.54
            print("Lin=" + str(longCM) + "/2.54=" + str(longIN) + "in")
        else:
            print("输入的数据有误，请确保最后两位是cm或in")
    except:
        print("输入的数据有误，请检查确保除最后两位外是数字")  # 异常处理


# 货币转换1美元=6.8743人民币
def changeCurrency(x):
    try:
        type = x[-1:]  # 截取最后一位单位
        if (type == "￥"):
            rmb = float(x[:-1])
            dollar = rmb / 6.8743
            print("C$=" + str(rmb) + "/6.8743=" + str(dollar) + "$")
        elif (type == "$"):
            dollar = float(x[:-1])
            rmb = dollar * 6.8743
            print("C$=" + str(dollar) + "*6.8743=" + str(rmb) + "￥")
        else:
            print("输入的数据有误，请确保最后一位是$或￥")
    except:
        print("输入的数据有误，请检查确保除最后一位外是数字")  # 异常处理


print("******************欢迎使用万能计算器******************")
print("T 温度转换")
print("L 长度转换")
print("C 货币转换")
# 菜单页面
userChoose = "y"
while userChoose == "y":
    changeType = input("请输入转换类型")
    if changeType == "T":
        temperature = input("请输入温度（示例：1C或1F）")
        changeTem(temperature)
    elif changeType == "L":
        long = input("请输入长度（示例：1in或1cm）")
        changeLon(long)
    elif changeType == "C":
        currency = input("请输入货币（示例：1￥或1$）")
        changeCurrency(currency)
    else:
        print("请输入正确的转类型")
    userChoose = input("是否继续，请输入y或n")
    while (userChoose != "y" and userChoose != "n"):  # 判断用户选择
        print("请确保您输入的是y或是n")

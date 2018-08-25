"""
1. 自动判断需要进行的运算：如输入1+1，进行加法运算输出结果。

2. 每个函数添加函数说明（docstring）

"""


def add(a, b):
    return a + b


def reduce(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def is_operator(e):
    """
    判断单个字符是否为运算符
    :param e:单个字符
    :return:True or False
    """

    opers = ["+", "-", "*", "/"]
    if e in opers:
        return True
    else:
        return False


def generateFormula(str1, str2, oper):
    """
        生成计算式的方法
       :param str1:运算符前的数字
       :param str2:运算符后的数字
       :param oper:运算符
       :return:返回计算式
    """
    if (oper == "+"):
        result = add(str1, str2)
        show = str(str1) + str(oper) + str(str2) + "=" + str(result)
    elif (oper == "-"):
        result = reduce(str1, str2)
        show = str(str1) + str(oper) + str(str2) + "=" + str(result)
    elif (oper == "*"):
        result = multiply(str1, str2)
        show = str(str1) + str(oper) + str(str2) + "=" + str(result)
    elif (oper == "/"):
        result = divide(str1, str2)
        show = str(str1) + str(oper) + str(str2) + "=" + str(result)
    return show


def calculate():
    """
    计算主函数，分割算式
    :return:
    """
    strInput = input("请输入算式：例如 1+1")
    oper = ""
    countOper = 0
    try:
        for i in strInput:
            if is_operator(i):
                oper = i
                countOper += 1
        if oper != "" and countOper == 1:
            str1 = strInput.split(oper)[0]  # 算式前半部分
            str2 = strInput.split(oper)[1]  # 算式后半部分
            show = generateFormula(float(str1), float(str2), oper)
            print(show)
        else:
            print("您没有输入运算符或者输入了过多的运算符,请重新输入")
            calculate()
    except:
        print("您的输入不符合规范，请检查后重新输入")
        calculate()


print("---------计算器---------")
calculate()

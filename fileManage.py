"""
1. 实现文件查找功能：输入指定目录，按照文件名、文件类型进行查找，将找到               的文件名输出到屏幕上

2. 实现保存文件信息功能：输入指定目录，将目录下所有文件的文件信息保存到files.txt         中，格式为“文件名     文件类型”（文件类型即文件后缀名，要做到两列对齐可运    用字符串的ljust()或rjust()方法）

3. 实现文件重命名功能：查找到用户指定的文件，根据输入的新文件名对文件进行重     命名操作，

4. 每个函数添加函数说明（docstring）
"""
import os


def findFile(inputPath):
    """

    :param inputPath: 输入路径
    :return: 输出找到的文件
    """
    files = os.listdir(inputPath)
    inputFileName = input("请输入文件名，例如xujiayang.txt或.txt或xu")
    if (inputFileName.find(".") > 0):
        fileName = inputFileName.split(".")[0]  # 记录文件名前缀
        fileType = inputFileName.split(".")[1]  # 记录文件名后缀
    else:
        fileName = inputFileName
        fileType = ""
    if inputFileName == "":
        print("输入不能为空")
        findFile(inputPath)  # 输入为空后回调
    elif not (fileName == "") and not (fileType == ""):
        for file in files:
            if file.endswith(fileType) and fileName in file:
                print(file)
    elif not (fileName == "") and fileType == "":
        for file in files:
            if fileName in file:
                print(file)
    elif fileName == "" and not (fileType == ""):
        for file in files:
            if file.endswith(fileType):
                print(file)


def saveFile(inputPath):
    """
    保存文件的方法,当指定路径有未知后缀名的文件会导致报错
    :param inputPath:路径
    :return:
    """
    files = os.listdir(inputPath)
    with open("files.txt", "w") as fp:
        for file in files:
            f1 = file.split(".")
            fp.write(f1[0].ljust(20) + f1[1] + "\n")


def renameFile(inputPath):
    """
    对文件进行重命名操作
    :param inputPath: 文件所在文件夹
    :return:
    """
    oldName = input("请输入原文件完整文件名，例如xujiayang.txt")
    newName = input("请输入新文件完整文件名，例如xujiayang.txt")
    if os.path.isfile(str(inputPath) + "/" + str(oldName)):
        os.rename(str(inputPath) + "/" + str(oldName), str(inputPath) + "/" + str(newName))
    else:
        print("原文件不存在，请仔细检查")
        print(str(inputPath) + "/" + str(oldName))
        renameFile(inputPath)


def mainMenu(inputPath):
    """
    主菜单实现方法
    :param inputPath:用户输入的路径
    :return:
    """
    print("请选择功能，按要求输入字母")
    inputType = input("F:文件查找，S:文件保存，R:文件名重命名")
    if (inputType == "F"):
        try:
            findFile(inputPath)
        except:
            print("找不到指定路径")
    elif (inputType == "S"):
        try:
            saveFile(inputPath)
        except:
            print("找不到指定路径,或指定路径有错误文件，请确保指定路径文件有完整后缀名")
    elif (inputType == "R"):
        renameFile(inputPath)
    else:
        print("选择有误，请按要求输入")
        mainMenu(inputPath)


print("-------------文件管理器----------------")
inputPath = input("请输入路径,例如C:/Users/vervain/Desktop/files")
mainMenu(inputPath)

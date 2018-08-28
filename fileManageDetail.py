import os


def findFile(inputPath):
    """

    :param inputPath: 输入路径
    :return: 输出找到的文件
    """
    fileList = {}
    files = os.listdir(inputPath)
    inputFileName = input("请输入文件名，例如xujiayang.txt或.txt或xu")
    if len(inputFileName) >= 2:
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
    else:
        print("查找关键字少于两字符 请重新输入")


def findPath():
    """
    查找用户输入的路径
    :return:
    """
    inputPath = input("请输入路径,例如C:/Users/vervain/Desktop/files")
    if os.path.isdir(inputPath):
        mainMenu(inputPath)
    else:
        while True:
            user_choose = input("路径不存在或不是文件夹请重新输入，y/n")
            if user_choose == "y":
                findPath()
                break
            elif user_choose == "n":
                exit()
    return inputPath


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
    rename_list = {}
    count = 1
    keyword = input("请输入需要修改的文件名关键字：")
    for file in os.listdir(inputPath):
        if keyword in file:
            rename_list[count] = file
            count += 1
    if len(rename_list) != 0:
        for key in rename_list:
            print(str(key) + ":" + rename_list[key])
        rename_order = int(input("请选择要重命名的文件序号: "))
        if rename_order in rename_list.keys():
            rename_file = rename_list[rename_order]
            filename_new = input("请输入新的文件名：")
            if len(filename_new) > 0:
                os.rename(inputPath + "/" + rename_file, inputPath + "/" + filename_new)
                print("修改成功")
            else:
                print("输入新名字不可为空")
        else:
            print("输入序号不存在 请重新操作")
    else:
        print("含此关键词的文件名不存在 请重新输入")


def mainMenu(inputPath):
    """
    主菜单实现方法
    :param inputPath:用户输入的路径
    :return:
    """
    print("请选择功能，按要求输入字母")
    inputType = input("F:文件查找，S:文件保存，R:文件名重命名")
    if (inputType == "F"):
        findFile(inputPath)
        while True:
            user_choose = input("是否继续进行当前操作文件夹，y/n")
            if user_choose == "y":
                mainMenu(inputPath)
            elif user_choose == "n":
                user_choose2 = input("是否切换路径,y/n")
                if user_choose2 == "y":
                    inputPath = findPath()
                elif user_choose2 == "n":
                    exit()

    elif (inputType == "S"):
        saveFile(inputPath)
        while True:
            user_choose = input("是否继续进行当前操作文件夹，y/n")
            if user_choose == "y":
                mainMenu(inputPath)
            elif user_choose == "n":
                user_choose2 = input("是否切换路径,y/n")
                if user_choose2 == "y":
                    inputPath = findPath()
                elif user_choose2 == "n":
                    exit()
    elif (inputType == "R"):
        renameFile(inputPath)
        while True:
            user_choose = input("是否继续进行当前操作文件夹，y/n")
            if user_choose == "y":
                mainMenu(inputPath)
            elif user_choose == "n":
                user_choose2 = input("是否切换路径,y/n")
                if user_choose2 == "y":
                    inputPath = findPath()
                elif user_choose2 == "n":
                    exit()
    else:
        print("选择有误，请按要求输入")
        mainMenu(inputPath)


print("-------------文件管理器----------------")

inputPath = findPath()
mainMenu(inputPath)

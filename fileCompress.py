"""
1. 将files_0827文件夹的所有文件以及子文件夹（file1,file2,file3,file4）的所有文件进行去重处理

2. 按文件类型在files_0827文件夹中创建以文件类型命名的子文件夹，将所有同类型文件（包括子文件夹中的文件）放入创建的文件夹中。

3. 将所有分类的文件夹做压缩处理，并删除原有文件夹。

"""
import os
import filecmp
import shutil

file_path = "./files_0827"


def get_all_files(path):
    """
    查找所有文件
    :param path: 文件夹根路径
    :return: 所有文件
    """
    all_files = []
    folders = os.listdir(path)
    for folder in folders:
        if os.path.isdir(file_path + "/" + folder):
            files = os.listdir(file_path + "/" + folder)
            for file in files:
                all_files.append(path + "/" + folder + "/" + file)

        else:
            all_files.append(path + "/" + folder)
    return all_files


def compare_files(x, y):
    """
    文件去重
    :param x:文件x
    :param y: 文件y
    :return:
    """
    if filecmp.cmp(x, y):
        # 如果x，y一致，删除y
        os.remove(y)
        print("重复文件已经被删除")


def compare_result(all_files):
    """
    遍历删除所有文件
    :param all_files: 所有文件
    :return:
    """
    for x in all_files:
        for y in all_files:
            if x != y and os.path.exists(x) and os.path.exists(y):
                compare_files(x, y)


def remove_file(files):
    """
    移动文件
    :param files: 所有文件
    :return: 生成的文件夹
    """
    type = set()  # 存放生成的文件夹
    for file in files:
        folder_name = file.split(".")[-1]
        # 查看一下文件夹是否存在，如果不存在，就创建
        folder_path = "./files_0827/" + folder_name
        if not os.path.exists(folder_path):
            # 创建文件夹,拼接路径join（）
            os.makedirs(folder_path)
            type.add(folder_name)
            # 移动文件到该文件夹下
            shutil.move(file, folder_path)
        else:
            # 如果文件夹存在，直接移动文件
            shutil.move(file, folder_path)
    return type


def delete_empty(dir):
    """
    删除空文件夹
    :param dir:
    :return:
    """
    if os.path.isdir(dir):
        for item in os.listdir(dir):
            delete_empty(os.path.join(dir, item))

        if not os.listdir(dir):
            os.rmdir(dir)
            print("移除空目录：" + dir)


def zip_all_files(types):
    """
    压缩文件并删除原来文件
    :param types:文件集合
    :return:
    """
    for type in types:
        zip_path = file_path + "/" + type
        output_path = file_path + "/"
        files = os.listdir(zip_path)
        zip_name = output_path + type
        shutil.make_archive(zip_name, "zip", zip_path)
        for file in files:
            os.remove(zip_path + "/" + file)


all_files = get_all_files(file_path)
compare_result(all_files)
now_files = get_all_files(file_path)
delete_empty(file_path)
type = remove_file(now_files)
zip_all_files(type)
delete_empty(file_path)

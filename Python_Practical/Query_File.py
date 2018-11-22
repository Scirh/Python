#Author Scon
# -*- coding utf-8 -*-
# help()

import os
#利用递归，实现对文件的遍历和查询
"""
首先需要输入一个文件路径，判断用户输入的是否是一个目录，如果是就重新调用函数，
如果不是就向列表中添加
"""

import os
all_file = []   # 创建字典存储查询到的值

def All_files(path):
    fliepath = os.listdir(path)   # 列出指定目录的文件

    for file in fliepath:
        filename = os.path.join(path,file)  # 将一个或多个路径正确地连接起来。
        #需要注意的是，需要加入原本的路径以及新产生的文件夹，这样才会将路径和*路径的任何成员的串联

        if os.path.isdir(filename):     # 判断查找的出来的是文件还是文件夹，如果是文件夹则重新#调用函数执行判断，如果不是则将查询的结果以追加的方式存储到列表中
            All_files(filename)
        else:
            all_file.append(filename)

    return all_file

if __name__ == '__main__':
    while True:
        try:
            file_path = input("Please enter the file that you want to query:").strip()
            data = All_files(file_path)
            print('\n',data,'\n')
        except NotADirectoryError:
            print("\n\033[44;30m'%s' is a file,Please enter the folder!\033[0m\n" % file_path)
        except FileNotFoundError:
            print("\n\033[31;1mInvalid Enter.Try again！\033[0m\n")
        except (KeyboardInterrupt,EOFError):
            break


# import os
# def all_file(path):
#
#     filelist = []
#     filename = os.walk(path)
#     for file in filename:
#         filelist.append(file)
#     return filelist
#
# if __name__ == '__main__':
#     while True:
#         try:
#             file_path = input("Please enter the file that you want to query:").strip()
#             data = all_file(file_path)
#             print('\n',data,'\n')
#         except NotADirectoryError:
#             print("\n\033[44;30m'%s' is a file,Please enter the folder!\033[0m\n" % file_path)
#         except FileNotFoundError:
#             print("\n\033[31;1mInvalid Enter.Try again！\033[0m\n")
#         except (KeyboardInterrupt,EOFError):
#             break

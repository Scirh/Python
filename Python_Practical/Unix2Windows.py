#Author Scon
# -*- coding utf-8 -*-
# help()


import sys
import os


class File_Coversion:
    'Convert File'

    def __init__(self, file):
        self.file = file

    def to_unix(self):

        unixflie = os.path.splitext(self.file)[0] + '_unix.txt'
        with open(self.file, 'r') as fwindowsobj:
            with open(unixflie, 'w') as funixobj:
                for line in fwindowsobj:
                    lines = line.rstrip() + '\n'
                    funixobj.write(lines)

    def to_windows(self):

        windowsfile = os.path.splitext(self.file)[0] + '_windows.txt'
        with open(self.file, 'r') as funixobj:
            with open(windowsfile, 'w') as fwindowsobj:
                for line in funixobj:
                    lines = line.rstrip() + '\r\n'
                    fwindowsobj.write(lines)


if __name__ == '__main__':
    while True:
        tips = """
        [1] Unix To Windows
        [2] Windows To Unix
        [3] Exit
        Please enter your choice (1/2/3):
        """
        try:
            choice = input(tips).strip()[0]
        except IndexError:
            print("\033[31;1mInvaild Input!\033[0m")
        except KeyboardInterrupt:
            break
        else:
            # 转换为windows格式
            if choice == '1':
                windows_file = input("\t \033[34;1mPlease enter you want to convert file :\033[0m")
                conversion = File_Coversion(windows_file)
                conversion.to_windows()
                print("\t\033[31;1mConvert Successful!\033[0m")
            # 转换为Unix格式
            elif choice == '2':
                unix_file = input("\t \033[34;1mPlease enter you want to convert file :\033[0m")
                conversion = File_Coversion(unix_file)
                conversion.to_unix()
                print("\t \033[31;1mConvert Successful!\033[0m")
            elif choice == "3":
                exit()
            else:
                print('\t',"\033[31;1mInvaild Input!\033[0m")

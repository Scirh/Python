# -*- coding: utf-8 -*-
# By Scong
# Date 2019-01-29
# Version 1.0.3


# 相关模块
import random
import string
import getpass

# 获得所有的字符串
all_char = string.ascii_letters + string.digits

# 定义随机生成密码函数
def get_pass(get_num):
    result = ""
	
	# 循环用户输入长度，最后输出随机密码
    for i in range(get_num):
        char = random.choice(all_char)
        result += char
    return result


if __name__ == '__main__':
    # 循环判断用户输入的信息，并捕获异常并处理
    while True:
        try:
               get_num = int(input("Please Enter the length of the password you want to generate:"))
               password = get_pass(get_num)
               print("The password is : %s"% (password))
               exit()
        except ValueError:
               print("\n\033[31;1m Please enter the correct password number!\033[0m\n")
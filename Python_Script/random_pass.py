# -*- coding utf-8 -*-
# By Scong
# Date 2019-01-29
# Version 1.0.1


# 随机密码生成器
import random
import string
import getpass

# 获得所有字符串
all_char = string.ascii_letters + string.digits + string.punctuation

# 定义随机密码函数
def get_pass(get_num):
    result = ""
    for i in range(get_num):
        char = random.choice(all_char)
        result += char
    return result


if __name__ == '__main__':

	#循环判断用户输入的是否为数字，如果不是则警告
   while True:
   # 异常处理
       try:
           get_num = int(input("请输入你要生成的密码长度："))
           password = get_pass(get_num)
           print("密码为：",password)
           exit()
       except ValueError:
           print("\n\033[31;1m请输入正确的密码位数！\033[0m\n")



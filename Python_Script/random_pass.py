# -*- coding utf-8 -*-
# By Scong
# Date 2019-01-29
# Version 1.0.0


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

# 用户自行获取密码长度
    get_num = int(input("请输入你要生成的密码长度:"))
	
# 调用函数
    password = get_pass(get_num)
	
# 打印随机密码
    print("密码为:", password)

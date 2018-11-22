# Author Scong
# -*- coding utf-8 -*-
# help()

# 猜拳游戏


# import random
#
# print("\t**************************")
# print("\t*                        *")
# print("\t*      Hey  Welcome!     *")
# print("\t*  游戏采用是三局两胜制  *")
# print("\t*  GoodLuck  Have Fun!   *")
# print("\t*                        *")
# print("\t**************************")
#
# mode = ['剪刀', '石头', '布']
# win_list = [['石头', '剪刀', ], ['剪刀', '布'], ['布', '石头']]
# prompt = """
# #\t[0] 剪刀
# #\t[1] 石头
# #\t[2] 布
# #\t请选择出拳的姿势：
#
# player_win = 0
# computer_win = 0
#
# while True:
#
#     computer = random.choice(mode)
#     ind = int(input(prompt))

#     if ind > 2:
#         print("\t\033[31;1m你的输入有误,请重新输入\033[0m")
#         continue
#     else:
#         player = mode[ind]
#
# #判断出拳胜负者以及胜利次数统计：
#     print(" \n       ****** Result ******      ")
#     print("\nPlayer:%s,Computer:%s" % (player, computer))
#     if player == computer:
#         print("\t\033[32;1m平局！再来一次！\033[0m")
#
#     elif [player,computer] in win_list:
#         print("'\t\033[31;1m甘拜下风，YOU WIN!!!\033[0m")
#         player_win += 1
#
#     else:
#         print("'\t'\n\033[34;1m手气不佳，YOU LOSE!!!\033[0m")
#         computer_win += 1
#
# #根据统计的胜负次数，判断三局两胜制谁胜谁负：
#
#     print("\nPlayer Win Count:",player_win,"\tComputer Win Count:",computer_win )
#     if player_win >= 3 and computer_win < 3:
#         print("\n\033[31;1m****** Player Win,Game Over!!! ******\033[0m")
#         print("\n\033[31;1m******        Bye              ******\033[0m")
#         exit()
#     elif computer_win >= 3 and  player_win < 3:
#         print("\n\033[35;1m****** Computer Win，GookLuck!!! ******\033[0m")
#         print("\n\033[35;1m******          Bye              ******\033[0m")
#         exit()


# 菲波那契数列
# def gen_fib(l):
#     fib = [0, 1]
#
#     for i in range(l - len(fib)):
#         fib.append(fib[-1] + fib[-2])
#
#     return fib  # 返回列表，不返回变量fib
#
# print('-' * 50)
# n = int(input("length: "))
# print(gen_fib(n))  # 不会把变量n传入，是把n代表的值赋值给形参


# 九九乘法表

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%s*%s=%s' % (j, i, i * j), end='\t')
#     print()


# 模拟cp操作

# import sys
#
# def copy(src_fname, dst_fname):
#     src_fobj = open(src_fname, 'rb')
#     dst_fobj = open(dst_fname, 'wb')
#
#     while True:
#         data = src_fobj.read(4096)
#         if not data:
#             break
#         dst_fobj.write(data)
#
#     src_fobj.close()
#     dst_fobj.close()
#
# copy(sys.argv[1], sys.argv[2])

# 模拟创建txt文件
# import os
#
# def get_fname():
#     while True:
#         fname = input('filename: ')
#         if not os.path.exists(fname):
#             break
#         print('%s already exists. Try again' % fname)
#
#     return fname
#
# def get_content():
#     content = []
#     print('输入数据，输入end结束')
#     while True:
#         line = input('> ')
#         if line == 'end':
#             break
#         content.append(line)
#
#     return content
#
# def wfile(fname, content):
#     with open(fname, 'w') as fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = ['%s\n' % line for line in content]
#     wfile(fname, content)

# 检查标识符

# import sys
# import keyword
# import string
#
# first_chs = string.ascii_letters + '_'
# all_chs = first_chs + string.digits
#
# def check_id(idt):
#     if keyword.iskeyword(idt):
#         return "%s is keyword" % idt
#
#     if idt[0] not in first_chs:
#         return "1st invalid"
#
#     for ind, ch in enumerate(idt[1:]):
#         if ch not in all_chs:
#             return "char in postion #%s invalid" % (ind + 2)
#
#     return "%s is valid" % idt
#
#
# if __name__ == '__main__':
#     print(check_id(sys.argv[1]))


# 创建用户并将用户信息写入到文本文件中

# 这里缺少生成随机密码
# import subprocess
# import sys
#
#
# def adduser(username, password, fname):
#     data = """user information:
# %s: %s
# """
#     subprocess.call('useradd %s' % username, shell=True)
#     subprocess.call(
#         'echo %s | passwd --stdin %s' % (password, username),
#         shell=True
#     )
#     with open(fname, 'a') as fobj:
#         fobj.write(data % (username, password))
#
# if __name__ == '__main__':
#     username = sys.argv[1]
#     password = gen_pass()
#     adduser(username, password, '/tmp/user.txt')


# 用列表构建栈结构

# stack = []
#
# def push_it():
#     item = input('item to push: ')
#     stack.append(item)
#
# def pop_it():
#     if stack:
#         print("from stack popped %s" % stack.pop())
#
# def view_it():
#     print(stack)
#
# def show_menu():
#     cmds = {'0': push_it, '1': pop_it, '2': view_it}
#     prompt = """(0) push it
# (1) pop it
# (2) view it
# (3) exit
# Please input your choice(0/1/2/3): """
#
#     while True:
#         # input()得到字符串，用strip()去除两端空白，再取下标为0的字符
#         choice = input(prompt).strip()[0]
#         if choice not in '0123':
#             print('Invalid input. Try again.')
#             continue
#
#if choice =="3":
#break
#
#         cmds[choice]()
#
#
# if __name__ == '__main__':
#     show_menu()


# 模拟实现Linux to windows 文本文件的格式转换

# import sys
#
# def unix2dos(fname):
#     dst_fname = fname + '.txt'
#
#     with open(fname) as src_fobj:
#         with open(dst_fname, 'w') as dst_fobj:
#             for line in src_fobj:
#                 line = line.rstrip() + '\r\n'
#                 dst_fobj.write(line)
#
#
# if __name__ == '__main__':
#     unix2dos(sys.argv[1])

# 编写类进度条

# import time
#
# length = 19
# count = 0
#
# while True:
#     print('\r%s@%s' % ('#' * count, '#' * (length - count)), end='')
#     try:
#         time.sleep(0.3)
#     except KeyboardInterrupt:
#         print('\nBye-bye')
#         break
#     if count == length:
#         count = 0
#     count += 1


# 自定义异常

# def set_age(name, age):
#     if not 0 < age < 120:
#         raise ValueError('年龄超过范围')
#     print("%s is %d years old" % (name, age))
#
# def set_age2(name, age):
#     assert 0 < age < 120, '年龄超过范围'
#     print("%s is %d years old" % (name, age))
#
# if __name__ == '__main__':
#     set_age('zhangsan', 20)
#     set_age2('lisi', 200)


# 实现简单的记账功能

# import pickle
# import os
# import time
#
#
# def cost(wallet, record):
#     amount = int(input('amount: '))
#     comment = input('comment: ')
#     date = time.strftime('%Y-%m-%d')
#     with open(wallet, 'rb') as fobj:
#         balance = pickle.load(fobj) - amount
#     with open(wallet, 'wb') as fobj:
#         pickle.dump(balance, fobj)
#     with open(record, 'a') as fobj:
#         fobj.write(
#             '%-12s%-8s%-8s%-10s%-20s\n' % (date, amount, '', balance, comment)
#         )
#
# def save(wallet, record):
#     amount = int(input('amount: '))
#     comment = input('comment: ')
#     date = time.strftime('%Y-%m-%d')
#     with open(wallet, 'rb') as fobj:
#         balance = pickle.load(fobj) + amount
#     with open(wallet, 'wb') as fobj:
#         pickle.dump(balance, fobj)
#     with open(record, 'a') as fobj:
#         fobj.write(
#             '%-12s%-8s%-8s%-10s%-20s\n' % (date, '', amount, balance, comment)
#         )
#
# def query(wallet, record):
#     print('%-12s%-8s%-8s%-10s%-20s' % ('date', 'cost', 'save', 'balace', 'comment'))
#     with open(record) as fobj:
#         for line in fobj:
#             print(line, end='')
#     with open(wallet, 'rb') as fobj:
#         balance = pickle.load(fobj)
#     print("Latest Balance: %d" % balance)
#
#
# def show_menu():
#     cmds = {'0': cost, '1': save, '2': query}
#     prompt = """(0) cost
# (1) save
# (2) query
# (3) exit
# Please input your choice(0/1/2/3): """
#     wallet = 'wallet.data'
#     record = 'record.txt'
#     if not os.path.exists(wallet):
#         with open(wallet, 'wb') as fobj:
#             pickle.dump(10000, fobj)
#
#     while True:
#         try:
#             choice = input(prompt).strip()[0]
#         except IndexError:
#             continue
#         except (KeyboardInterrupt, EOFError):
#             print()
#             choice = '3'
#
#         if choice not in '0123':
#             print('Invalid input. Try again.')
#             continue
#
#         if choice == '3':
#             break
#         cmds[choice](wallet, record)
#
# if __name__ == '__main__':
#     show_menu()


# 简单的加减法数学游戏


# from random import randint, choice
#
# def exam():
#     cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
#     nums = [randint(1, 100) for i in range(2)]
#     nums.sort(reverse=True)
#     op = choice('+-')
#     result = cmds[op](*nums)
#     prompt = "%s %s %s = " % (nums[0], op, nums[1])
#     tries = 0
#
#     while tries < 3:
#         try:
#             answer = int(input(prompt))
#         except:
#             continue
#
#         if answer == result:
#             print('Very good!')
#             break
#         else:
#             print('Wrong answer.')
#             tries += 1
#     else:
#         print('%s%s' % (prompt, result))
#
# if __name__ == '__main__':
#     while True:
#         exam()
#         try:
#             yn = input("Continue(y/n)? ").strip()[0]
#         except IndexError:
#             continue
#         except (KeyboardInterrupt, EOFError):
#             print()
#             yn = 'n'
#
#         if yn in 'nN':
#             break


# 简单的GUI程序

# import tkinter
# from functools import partial
#
# def hello(word):
#     def welcome():
#         lb.config(text="Hello %s!" % word)
#     return welcome  # hello函数的返回值还是函数
#
# root = tkinter.Tk()
# lb = tkinter.Label(text="Hello world!", font="Times 26")
# MyBtn = partial(tkinter.Button, root, fg='white', bg='blue')
# b1 = MyBtn(text='Button 1', command=hello('China'))
# b2 = MyBtn(text='Button 2', command=hello('tedu'))
# b3 = MyBtn(text='quit', command=root.quit)
# lb.pack()
# b1.pack()
# b2.pack()
# b3.pack()
# root.mainloop()


# 实现递归排序

# from random import randint
#
# def quick_sort(num_list):
#     if len(num_list) < 2:
#         return num_list
#
#     middle = num_list[0]
#     smaller = []
#     larger = []
#     for i in num_list[1:]:
#         if i < middle:
#             smaller.append(i)
#         else:
#             larger.append(i)
#
#     return quick_sort(smaller) + [middle] + quick_sort(larger)
#
# if __name__ == '__main__':
#     alist = [randint(1, 100) for i in range(10)]
#     print(alist)
#     print(quick_sort(alist))

# hashlib模块进行文件的校验

# import hashlib
#
# in_file = input("Please enter want to check file:")
#
# def check_flie(filename):
#     with open(filename,'rb') as fobj:
#         data = fobj.read()
#
#     m = hashlib.md5()
# #    m = hashlib.md5(data)      # 如果文件过大，在校验的过程中会出现占用资源，所以需要一部分的读取
#     m.update(data)          # 读取部分文件进行校验
#     print('\nMD5Sum:\033[31;1m%s\033[0m' % (m.hexdigest()))
#
# if __name__ == '__main__':
#     check_flie(in_file)


#文件的压缩与解压:
# import tarfile
#
# #压缩文件:
# with tarfile.open('/mnt/demo.tar.gz','w:gz') as fobj:
#     fobj.add('/etc/passwd')
#     fobj.add('/etc/hosts')
#
# #解压文件:
# with tarfile.open('/mnt/demo.tar.gz') as fobj:
#     fobj.extractall()

# 面向对象_类

# class BearToy:
#     def __init__(self,color,size):  #__init__在实例化自动执行,实例本身自动作为第一个参数传递给self
#
#         self.color = color       # 绑定属性到实例
#         self.size = size
#
#
# if __name__ == '__main__':
#     tidy = BearToy('brown','small')     # 调用__init__
#     print(tidy.color)
#     print(tidy.size)


# 面向对象_类的组合

# class productor:
#     def __init__(self,tel,email,addresses):
#         self.tel = tel
#         self.email = email
#         self.addresses = addresses
#
#     def info(self):
#         print("这只熊生产商的地址是:%s\n电话是:%s" % ((self.addresses,self.tel)))
#
# class BearToy:
#     def __init__(self,color,size,tel,email,addresses):
#
#         self.color = color
#         self.size = size
#         self.vendor = productor(tel,email,addresses)
#
# if __name__ == '__main__':
#     tidy = BearToy('brown','small','14546544','123@123.com','广东广州')
#     print(tidy.color,'\n')
#     tidy.vendor.info()

# 面向对象_类的子类继承以及多重继承

# class BearToy:
#     def __init__(self,color,size):
#
#         self.color = color
#         self.size = size
#
# class newBear(BearToy): # 多重继承只要在添加多一个类即可
#
#     def __init__(self,color,size,date):
#         super(newBear,self).__init__(color,size)
# # 如果子类中有和父类同名的方法,父类方法将会被覆盖,如果需要访问父类的方法,则要使用super,明确的指出父类
#         self.date = date
#
#     def run(self):
#         print("running ... ... ")
#         print(
#             "This bear's color is '%s' ,the size is '%s',product for '%s'"
#              % (self.color,self.size,self.date)
#               )
#
# if __name__ == '__main__':
#     tidy = newBear('brown','small',2018-7-1)
#     tidy.run()

#类方法
# class Date:
#     def __init__(self,year,month,date):
#         self.year = year
#         self.month = month
#         self.date = date
#
#     @classmethod        # 类方法,不用创建实例即可调用
#     def create_date(cls,string_date):
#         y, m, d, = map(int,string_date.split('-'))
#         dt = cls(y,m,d)
#         return dt
#
# if __name__ == '__main__':
#     birth_date = Date(1995,4,12)
#     day = Date.create_date('2018-5-1')
#     print(day)

#编写酒店类

# class Hotel:
#     def __init__(self,price = 200,cuttoff = 1.0,bf = 15):
#         self.price = price
#         self.cuttoff = cuttoff
#         self.bf = bf
#
#     def tatol(self,days = 1):
#         return (self.price * self.cuttoff + self.bf) * days
#
# if __name__ == '__main__':
#     stdroom = Hotel()
#     bigroom = Hotel(200,0.8)
#     print(stdroom.tatol())
#     print(stdroom.tatol(2))
#     print(bigroom.tatol())
#     print(bigroom.tatol(2))


# print(Hotel.__doc__)        # 查看类的文档字符串(备注信息)
# print(Hotel.__name__)       # 查看类名
# print(Hotel.__dict__)       # 查看类的属性

#编写书籍类
# class Book:
#     def __init__(self,title,author,pages):    # 实例化实例时默认会调用的方法
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):          # 创建打印/现实实例时调用的方法
#         return "<%s> " % self.title
#
#     def __call__(self):         # 创建可调用的实例
#         print("%s is by %s" % (self.title,self.author))
#
# if __name__ == '__main__':
#     py_book = Book('Python','Wysley',800)
#     print(py_book)      # 调用__str__
#     py_book()       # 调用__call__


# import qrcode
# import image
#
# qr = qrcode.QRCode(
#     version=1,
#     error_correction = qrcode.constants.ERROR_CORRECT_L,
#     box_size = 10,
#     border = 2,
# )
# url = 'http://www.baidu.com'
# qr.add_data(url)
# img = qr.make_image()
# img.save('1.png')


#TCP创建客户端
import socket
import time

host = '192.168.4.254'
port = 7296
addr = (host,port)

c = socket.socket()
c.connect(addr)
while True:

    dt = time.strftime('%Y-%m-%d %X', time.localtime())
    data = dt + ' ---> ' + input('-> ')
    c.send(data.encode('utf8'))
    if data.strip() == 'end':
        break
    data = c.recv(1024)
    print(data.decode('utf8'))

c.close()














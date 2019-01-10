#Author Scong
# -*- coding utf-8 -*-
#help()

'''
if -0.0:
    print('yes')    #不打印，任何值为0的数字都是False

if [1,2]:
    print('yes')    # 非空对象都是True

if ' ':
    print('yes')    #空格也是字符，所以条件为True '''


'''
a = 10
b = 20
if a < b:
    smaller = a
else:
    smaller = b
print(smaller)
    # ||
    # ||等价于
    # ||
smaller = a if a < b else b
print(smaller)'''


#模拟用户登陆登陆

'''
import getpass

print("Please register your username and password!")
username = input("Username:")
password = getpass.getpass("Password：")
print("\nRegistered Successful !")

print("\nPlease Login!\n")
name=input("Username:")
passwd=getpass.getpass("Password:")

if (name == username and passwd == password):
    print("Login Successful")
elif passwd != password:
    print("Faild，Password mistake！")
else:
    print("User not exist!!!")'''

#因为pycharm无法控制终端，所以在使用了getpass模块也还是显示明文密码，且还会有报错，（错误不影响调试）。
# 如果想要看到效果，在linux的终端执行即可!


#竞猜数字：
'''
import random

number = random.randint(1,10)
for i in range(3):
    num = int(input("Guess a number(1-10):"))
    if num > number:
        print("猜大了！")
    elif num == number:
        print("恭喜，猜对了！")
        break
       # exit()
    else:
        print("猜小了！")
print("The number is:",number)'''


#猜拳游戏1.0
'''
import random

mode = ['剪刀','石头','布']
computer = random.choice(mode)

def jiandao():
    if computer == '剪刀':
        print("平局!")
    elif computer == '石头':
        print("YOU LOSE！")
    else:
        print("YOU WIN!")
def shitou ():
    if computer == '剪刀':
        print("YOU WIN!")
    elif computer == '石头':
        print("平局！")
    else:
        print("YOU LOSE!")
def bu():
    if computer == '剪刀':
        print("YOU LOSE！")
    elif computer == '石头':
        print("YOU WIN!")
    else:
        print("平局!")

print("\t**************************")
print("\t*                        *")
print("\t*        Welcome!!!      *")
print("\t*  该游戏采用的是三局两胜制  *")
print("\t*                        *")
print("\t**************************")

for i in range(3):
    player = input("\n请输入出拳的姿势：")
    print("\nPlayer:%s,Computer:%s" % (player, computer))
    if player == '剪刀':
        jiandao()
    elif player == '石头':
        shitou()
    elif player == '布':
        bu()
    else:
        print("请输入'剪刀''石头''布'三种出拳姿势！！！")
        exit()
'''


#猜拳游戏2.0
'''
import random

print("\t**************************")
print("\t*                        *")
print("\t*        Welcome!!!      *")
print("\t*  该游戏采用的是三局两胜制  *")
print("\t*                        *")
print("\t**************************")
mode = ['剪刀','石头','布']
computer = random.choice(mode)
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]

for i in range(3):
    player = input("\n\t请输入出拳的姿势：")
    print("\nPlayer:%s,Computer:%s" % (player, computer))
    if player == computer:
        print("平局！")
    elif [player,computer] in win_list:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
'''

#猜拳游戏3.0

'''
import random

print("\t**************************")
print("\t*                        *")
print("\t*        Welcome!!!      *")
print("\t*  该游戏采用的是三局两胜制  *")
print("\t*                        *")
print("\t**************************")


mode = ['剪刀','石头','布']
computer = random.choice(mode)
prompt = """
[0] 剪刀
[1] 石头
[2] 布
请选择（0/1/2）:"""
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]

for i in range(3):

    ide = int(input(prompt))
    if ide > 2:
        print("\033[31;1m输入有误，请重新输入！！!\033[0m")
        continue
    # elif ide  " ":
    #     print("\033[31;1m输入有误，请重新输入！！!\033[0m")
    #     continue
    else:
        player = mode[ide]

    print("\nPlayer:%s,Computer:%s" % (player, computer))

    if player == computer:
        print('\033[32;1m平局！\033[0m')
    elif [player,computer] in win_list:
        print('\033[31;1mYOU WIN!\033[0m')
    else:
        print('\033[34;1mYOU LOSE!\033[0m')
'''

#猜拳游戏4.0
import random

print("\t**************************")
print("\t*                        *")
print("\t*      Hey  Welcome!     *")
print("\t*  游戏采用是三局两胜制  *")
print("\t*  GoodLuck  Have Fun!   *")
print("\t*                        *")
print("\t**************************")

mode = ['剪刀', '石头', '布']
win_list = [['石头', '剪刀', ], ['剪刀', '布'], ['布', '石头']]
prompt = """
\t[0] 剪刀
\t[1] 石头
\t[2] 布
\t请选择出拳的姿势："""

player_win = 0
computer_win = 0

while True:

    computer = random.choice(mode)
    ind = int(input(prompt))

    if ind > 2:
        print("\t\033[31;1m你的输入有误,请重新输入\033[0m")
        continue
    else:
        player = mode[ind]

#判断出拳胜负者以及胜利次数统计：
    print(" \n       ****** Result ******      ")
    print("\nPlayer:%s,Computer:%s" % (player, computer))
    if player == computer:
        print("\t\033[32;1m平局！再来一次！\033[0m")

    elif [player,computer] in win_list:
        print("'\t\033[31;1m甘拜下风，YOU WIN!!!\033[0m")
        player_win += 1

    else:
        print("'\t'\n\033[34;1m手气不佳，YOU LOSE!!!\033[0m")
        computer_win += 1

#根据统计的胜负次数，判断三局两胜制谁胜谁负：

    print("\nPlayer Win Count:",player_win,"\tComputer Win Count:",computer_win )
    if player_win >= 3 and computer_win < 3:
        print("\n\033[31;1m****** Player Win,Game Over!!! ******\033[0m")
        print("\n\033[31;1m******        Bye              ******\033[0m")
        exit()
    elif computer_win >= 3 and  player_win < 3:
        print("\n\033[35;1m****** Computer Win，GookLuck!!! ******\033[0m")
        print("\n\033[35;1m******          Bye              ******\033[0m")
        exit()


#循环结构
'''
num=0
sum=0

while num <= 100:
    num +=1
    if num % 2:
        continue
    sum = num + sum     # 选中两行，组合键shift+tab 往左偏移，单个tab往右缩进
    # num += 2
print("100内偶数之和:",sum)
'''





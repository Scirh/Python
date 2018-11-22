#Author Scon
# -*- coding utf-8 -*-
# help()

import random

user_list = {}

def login():

    while True:
        username = input("\tUsername:")
        password = input("\tPassword:")
        if username not in user_list:
            print("\t\n\033[31;1m'%s' user is not exists.Please check again!\033[0m" % username)

        elif password != user_list[username]:
            print("\t\n\033[31;1mPassword is error!\033[0m")

        else:
            print("\t\033[31;1mLogin Successsful!\033[0m")
            break

def regis():
    username = input("\tUsername:")
    password = input("\tPassword:")

    if username in  user_list:
        print("\t'%s' user is exists.Please Try again." % username)
    else:
        user_list[username] = password
        print("\t\033[31;1mRegis user Successful!\033[0m")

    return user_list

def menu():

    cmds = {'1':regis,'2':login,'3':exit}
    Tips ="""
    [1] Regis
    [2] Login
    [3] Exit
    Please enter your choice(1/2/3):
    """
    while True:
        try:
            choice = input(Tips).strip()[0]

        except (KeyboardInterrupt,EOFError):
            exit()
        except IndexError:
            print("\t\033[31;1mPlease enter your choice.Try again.\033[0m")

        cmds [ 选择 ] （)



if __name__ == '__main__':
    menu()

#Author Scon
# -*- coding utf-8 -*-
# help()



import os

def get_fname():
    while True:
        try:
            tip = 'Notice'
            print("\n\033[31;1m %30s \033[0m" % tip)
            print("If no absolute path is entered, the generated file will in the program directory\n")
        except KeyboardInterrupt:
            break
        fname = input('Please enter the filename: ')
        if not os.path.exists(fname):
            break
        print('\n\033[31;1m"%s" already exists. Try again\n\033[0m' % fname)
    return fname

def get_content():
    content = []
    print('\nPlease enter data,and enter \033[31;1m"end"\033[0m to stop  ')
    while True:
        line = input('\033[31;1m->\033[0m\033[34;1m ~\033[0m ')
        if line == 'end':
            print("GoodBye!")
            break
        content.append(line)
    return content

def writefile(fname, content):
    try:
        with open(fname, 'w') as fobj:
            fobj.writelines(content)
    except FileNotFoundError:
        print("\n\033[31;1mInvalid Enter.Please enter the file path\033[0m")

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ['%s\n' % line for line in content]
    writefile(fname, content)
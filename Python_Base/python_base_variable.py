#Author Scong
# -*- coding utf-8 -*-

if 3 > 0:
    print("True")
else:
    print("False")

print("hello","Scong",sep="**") #sep="**" 表示以**进行分割，默认逗号是一个空格分开
print("hello Scong",end="") # end= 表示不要回车


# name = input("\nPlease your username:") #通过input获得的值，均为字符（str）,在做运算的时候，字符和数字不可以作运算
# print("Welcome",name)

print("\n",5 / 2)
print(5 // 2) #丢弃余数,只保留商
print(5 ** 3)   #5的3次方
print("***" * 50)   #打印50次
print(20 > 10 > 5)  #等价于 print(20 > 10 and 10 > 5 ),python支持连续比较
print(not 20 > 10)  #取反
print(5 % 2)    #取余



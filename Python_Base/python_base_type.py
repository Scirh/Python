#Author Scong
# -*- coding utf-8 -*-
#help()


#三个连续的单引号或者双引号，可以保存输入格式
'''
sentence="""hello
world
and
welcome"""
print(sentence)'''


#字符串的切片
'''
str="python"
print(str[2:4])     #字符串的截取，起始下标包含，结束下标不包含
print(str[::2])     #步长为2进行截取,默认是1
print(str[1::2])    #步长为2进行截取
print(str[::-1])    #步长为负，表示自右向左截取'''


#列表
'''
list1 = [1,2,3,4,5,6,'a','leexiaomei','c',[10,20,30]]
print(len(list1))   #打印列表的长度
print(list1[-1][-1])    #截取list1列表中的最后一个，然后在截取出来的结果上，截取最后一个
print(list1[7][3:])
list1.append("Scong")   #向列表追加元素
print(list1)
del list1[0]        #删除下标0的元素
print(list1)
list2=[1,344,5,6,7,433,0]
print(max(list2))'''

#字典,是key-value（键值对形式存在的，没有顺序，通过键取出值）
mydir = {'name':'lee','age':21}
print("长度为：\t",len(mydir))
print("名字：\t", mydir['name'] + "\n年龄：\t",mydir['age'])

# blist = alist		# 表示将alist的值赋值给blist，指向的都是同一内存空间的值，所以修改了blist的值，alist的值也会跟着改变
# clist = alist[:]	# 将alist的元素赋值给alist，此时clist，就会在内存空间中开辟新的空间进行存储，修改clist的元素，不会影响alist的

# id(clist)		#查找变量的身份位置

# 数据类型的分类
#按存储模型分类：
	#标量类型：数字，字符串
	#容器类型：列表，元组，字典
#按更新模型分类：
	#可变类型：列表，元组，字典
	#不可变类型：数字，字符串
#按访问模型分类：
	#直接访问：数字
	#顺序访问：字符串，列表，元组
	#映射访问：字典










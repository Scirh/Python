# -*- coding: utf-8 -*-
# By Scong
# Date 2019-03-27
# Version 1.0.0


person = []
def New_List(new_list):
    """
    最新人员名单
    :param list: 人员名单列表
    :return:
    """
    # 循环遍历在职人员名单，并将其写入至person列表
    for line in open(new_list, encoding='UTF-8'):
        rs = line.replace('\n', '')
        person.append(rs)
    return person

def Old_List(old_list):
    """
    旧的人员名单
    :param old_list: 人员名单列表
    :return:
    """
    person2 = []
    for line2 in open(old_list, encoding='UTF-8'):
        rs1 = line2.replace('\n', '')
        # 判断需求人员是否在在职人员列表内，不在则写入至person2列表
        if rs1 not in person:
            person2.append(rs1)
    return person2

if __name__ == '__main__':
    New_List("在职人员.txt")
    print(Old_List('旧的在职人员名单.txt'))
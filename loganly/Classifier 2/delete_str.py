# -*- coding: utf-8 -*-
# @Time : 2019/7/18 10:57
# @Author : Max
# @FileName: head.py
# @IDE: PyCharm


# 字符串删除算法一：通过列表
def delete_substr_method1(in_str, in_substr):
    start_loc = in_str.find(in_substr)
    in_str, in_substr = list(in_str), list(in_substr)
    [len_str, len_substr] = len(in_str), len(in_substr)
    res_str = in_str[:start_loc]
    for i in range(start_loc + len_substr, len_str):
        res_str.append(in_str[i])
    res = ''.join(res_str)
    return res


# 字符串删除算法二：通过切片
def delete_substr_method2(in_str, in_substr):
    start_loc = in_str.find(in_substr)
    len_substr = len(in_substr)
    res_str = in_str[:start_loc] + in_str[start_loc + len_substr:]
    return res_str


def get_pure_8583(head,tail,line):
    return delete_substr_method2(delete_substr_method2(line,head),tail)


if __name__ == '__main__':
    in_str = input("please input string:")
    in_substr1 = input("please input the first substring:")
    in_substr2 = input("please input the second substring:")
    result = delete_substr_method2(delete_substr_method2(in_str, in_substr1), in_substr2)
    print(result)
    print("ok")

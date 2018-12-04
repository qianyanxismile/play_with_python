#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import reduce


def count_with_reduce(d):
    """使用reduce统计"""
    return reduce(lambda a, b: a+b, map(lambda item: len(list(filter(lambda kk: kk!='0', item))), d.values()))


def str_count_optimization(d):
    """str_count优化版本，使用计数方式统计"""
    count = 0
    for v in d.values():
        for i n v:
            if i != '0':
                count += 1
    return count


def str_count(d):
    l=[]
   
    for v  in d.values():
        for i in v:
            if i != "0":
                l.append(i)
    print(len(l))

if __name__ =="__main__":
    d = {0 : ['1054', '2003', '0', '0', '0', '0'], 1 : ['1041', '2031', '0', '0', '0', '0']}
    str_count(d)

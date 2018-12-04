#!/usr/bin/python
# -*- coding: utf-8 -*-

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
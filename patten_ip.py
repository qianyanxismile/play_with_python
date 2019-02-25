# coding=utf-8

import re


def is_legal(match_ip):
    if match_ip:
        print "合法"
    else:
        print "非法"


if __name__ == '__main__':
    ip_test = raw_input("请输入IP:")
    patten_test = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    match_re = re.match(patten_test,ip_test)
    is_legal(match_re)

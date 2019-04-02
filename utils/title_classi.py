#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def test_findStr(name, target):
    if target.find(name):
        print("1")
    else:
        print("0")



if __name__ == '__main__':
    name = "调解书"
    target = "民事调解书"
    test_findStr(name, target)
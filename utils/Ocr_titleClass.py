#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
对于OCR的识别结果，进行全文本匹配，来识别关键词
"""
import re
import os

# 读取文件内容
def read_file(path):
    f = open(path, 'r', encoding='utf-8')
    text = f.read()
    # print(text)
    return text

# 匹配是否有如下关键词
def find_key(text):
    num = 0
    pattern = re.compile(u'宣判笔录|笔录')
    # print(pattern)
    # PATTERN = re.compile(ur'上诉')
    res = re.findall(pattern, text)
    print(res)
    if len(res):
        num = 1
    # for c in text:
    #     if c == "姚":
    #         num = 1
    #         break
    return num

def test_folder():
    path_in = "F:\Test\out\\tXPBL"
    # 获取路径下的所有文件
    text_list = os.listdir(path_in)
    num = 0
    file_num = 0

    for text in text_list:
        # print(text)
        # print(os.path.splitext(text)[-2][-3:])
        if os.path.splitext(text)[-2][-3:] == "jpg":
            file_num += 1
            print("file_num", file_num)
            path_long = os.path.join(path_in, text)
            print(path_long)
            text2 = read_file(path_long)
            num += find_key(text2)
    print("num", num)
    print(num / file_num)


def test_folder2():
    path_in = "F:\Test\out"
    path_out = "F:\Test\pre_out"
    num = 0
    folder_list = os.listdir(path_in)
    for folder in folder_list:
        file_list = os.listdir(os.path.join(path_in,folder))
        for file in file_list:
            num += 1
            print(file)
    print("num", num)
if __name__ == '__main__':
    test_folder2()
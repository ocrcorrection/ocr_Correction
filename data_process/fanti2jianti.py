# -*- coding: utf8 -*-
import os
from tqdm import tqdm
def test_opencc():
    import opencc
    cc = opencc.OpenCC('t2s')
    print(cc.convert(u'Open Chinese Convert（OpenCC）「開放中文轉換」，是一個致力於中文簡繁轉換的項目，提供高質量詞庫和函數庫(libopencc)。'))

from zhtools.langconv import *

def Traditional2Simplified(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence

def T2S_test():
    traditional_sentence = '憂郁的臺灣烏龜'
    simplified_sentence = Traditional2Simplified(traditional_sentence)
    print(simplified_sentence)

import re
# 正则匹配
# 讲错误的字替换为相应的正确的字
def find_text(text):
    word_dic = {}
    # m = re.match(u'<ESSAY title')
    reg = re.compile('<ESSAY title')
    # print(re.findall(u"<ESSAY title=\"(.+?)\">", text))
    sen_list = []
    for i in range(len(text)):

        if text[i].startswith("<PASSAGE"):
            sen_list.append(text[i][24:-11])
        elif text[i].startswith("<WRONG>") and text[i+1].startswith("<CORRECTION>"):
            word_dic[text[i][7:-9]] = text[i+1][12:-14]
    # print(sen_list)
    # print(word_dic)
    return sen_list, word_dic

# 语料替换,遍历原始语料库，如果在实体词典中存在，就替换，并且作为value值
def match_str(sen_list, word_dic):
    sen_dic = {}
    for c in sen_list:
        # print(c)
        for w in word_dic.keys():
            # print(w)
            if c.find(w) > 0:
                # print(w, word_dic[w])
                temp = c.replace(w, word_dic[w])
                # print(temp)
                sen_dic[c] = temp
                # break
    print(sen_dic)
    return sen_dic

def write_to_txt(file_path, sen_dict):
    with open(file_path, 'a', encoding='utf-8') as f:
        for c in sen_dict:
            f.write(c+" "+sen_dict[c])
            f.write('\n')


def write_to_txt2(file_path, sen_dict):
    with open(file_path, 'a', encoding='utf-8') as f:
        count = 0
        for src, dst in sen_dict.items():
            f.write('src: ' + ' '.join(dst) + '\n')
            f.write('dst: ' + ' '.join(src) + '\n')
            count += 1
        print("save line size:%d to %s" % (count, sen_dict))

# 读取文件内容
def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.readlines()
    # print(text)
    return text

# 读取文件夹中文件内容
def read_dir(dir):
    # text_list = []
    # for text in os.listdir(dir):
    #     print(text)
    #     text_list.append(text)
    return os.listdir(dir)

import os
# 测试下句子
def T2S(file_path="/Users/stone/Documents/数据/public_data/Training/SIGHAN15_CSC_A2_Training.sgml"):
    # Todo
    traditional_text = read_file(file_path)
    sim_list = []
    for c in traditional_text:
        simplified_sentence = Traditional2Simplified(c)
        sim_list.append(simplified_sentence)
    # print(sim_list)
    s, d = find_text(sim_list)
    # print(s)
    # print(d)
    file_path = "../data/taiwan_spell.txt"
    write_to_txt(file_path, match_str(s, d))

def union_format(file_path="/Users/stone/Documents/数据/public_data/Training/SIGHAN15_CSC_B2_Training.sgml", out_path = "../data/SIGHAN15_CSC_B2_Training_process.txt"):
    # Todo
    traditional_text = read_file(file_path)
    sim_list = []
    for c in traditional_text:
        simplified_sentence = Traditional2Simplified(c)
        sim_list.append(simplified_sentence)
    # print(sim_list)
    s, d = find_text(sim_list)
    # print(s)
    # print(d)
    write_to_txt2(out_path, match_str(s, d))

# 匹配sighan新版
def match_sighan(text):
    word_dic = {}
    # m = re.match(u'<ESSAY title')
    reg = re.compile('<ESSAY title')
    # print(re.findall(u"<ESSAY title=\"(.+?)\">", text))
    sen_list = []
    for i in range(len(text)):

        if text[i] == "<TEXT>":
            sen_list.append(text[i+1])
        elif text[i].startswith("<WRONG>") and text[i + 1].startswith("<CORRECTION>"):
            word_dic[text[i][7:-8]] = text[i + 1][12:-13]
    # print(sen_list)
    # print(word_dic)
    return sen_list, word_dic

# 匹配sighan新版，train版
def match_sighan2(text):
    word_dic = {}
    # m = re.match(u'<ESSAY title')
    reg = re.compile('<ESSAY title')
    # print(re.findall(u"<ESSAY title=\"(.+?)\">", text))
    sen_list = []
    for i in range(len(text)):
        if text[i].startswith("<TEXT>"):
            sen_list.append(text[i][6:-7])
        elif text[i].startswith("<WRONG>") and text[i + 1].startswith("<CORRECTION>"):
            word_dic[text[i][7:-8]] = text[i + 1][12:-13]
    # print(sen_list)
    # print(word_dic)
    return sen_list, word_dic

def union_format_dir(dir_path="/Users/stone/Documents/correction_data/sighan bake-off/train",
                     out_path = "/Users/stone/Documents/correction_data/sighan bake-off processed/sighan_output_train.txt"):
    # Todo
    traditional_text_list = os.listdir(dir_path)
    sim_list = []
    print(traditional_text_list)
    sen_count = 0 # 统计句子个数
    for text in tqdm(traditional_text_list):
        traditional_text = read_file(os.path.join(dir_path, text))
        # print("traditional_text", traditional_text)
        for c in tqdm(traditional_text):
    #         print(c)
            simplified_sentence = Traditional2Simplified(c)
            sim_list.append(simplified_sentence.strip())
            sen_count += 1
    print(sim_list)
    print("count:", sen_count)
    # s:source; d:target
    s, d = match_sighan2(sim_list)
    print(s)
    print(d)
    write_to_txt2(out_path, match_str(s, d))

if __name__=="__main__":
    # T2S_test()
    # T2S()
    # union_format()
    test_path = "/Users/stone/Documents/correction_data/sighan bake-off/test"
    train_path = "/Users/stone/Documents/correction_data/sighan bake-off/train"
    test_out = "/Users/stone/Documents/correction_data/sighan bake-off processed/sighan_output_test.txt"
    train_out = "/Users/stone/Documents/correction_data/sighan bake-off processed/sighan_output_train.txt"
    # union_format_dir(dir_path=test_path, out_path=test_out)
    union_format_dir(dir_path=train_path, out_path=train_out)
    # union_format_dir(dir_path="/Users/stone/Documents/correction_data/sighan_test",
    #                  out_path="/Users/stone/Documents/correction_data/test2.txt")
    # dir_path = "/Users/stone/Documents/correction_data/sighan_test/test13.sgml"
    # read_file(dir_path)
    # path = "/Users/stone/Documents/correction_data/sighan bake-off"
    # read_dir(path)


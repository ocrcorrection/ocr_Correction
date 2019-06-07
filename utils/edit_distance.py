#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import Levenshtein


def minD(texta, textb):
    # texta = u"我好你好hajkshd,"
    # textb = u"我好你"
    print(Levenshtein.distance(texta, textb))

# https://blog.csdn.net/HappyRocking/article/details/86491042
def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    动态规划。
    """
    m = len(word1)
    n = len(word2)
    # 初始化，D(i,0)=i, D(0,j)=j
    D = [[0] * (n+1) for _ in range(m+1)]
    D[0] = [i for i in range(n+1)]
    for i in range(m+1):
        D[i][0] = i
    # 迭代
    for i in range(1,m+1):
        for j in range(1,n+1):
            tmp1 = min(D[i-1][j], D[i][j-1]) + 1
            tmp2 = D[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1)
            D[i][j] = min(tmp1, tmp2)
    return D[m][n]

if '__main__' == __name__:
    word1 = "你好啊地方和毒害的数据库"
    word2 = "你好啊地方"
    minD(word1, word2)
    print(minDistance(word1, word2))


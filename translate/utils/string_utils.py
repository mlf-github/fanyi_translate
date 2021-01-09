#!/usr/bin/python
# coding=utf-8
import re
import sys

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

en_pattern = re.compile('[a-zA-Z]+')

# 原创
def my_split(string, seps=[]):
    # remove ""
    while "" in seps:
        seps.remove("")

    temps1 = []
    temps1.extend(string.split(seps[0]))

    i = 0
    tempss = [temps1]
    for i in range(1, len(seps)):
        tempss.append([])
        for temp in tempss[i-1]:
            tempss[i].extend(temp.split(seps[i]))

    while "" in tempss[i]:
        tempss[i].remove("")
    splits = tempss[i]
    return splits

def contain_zh(word):
    if word is None:
        return False
    word = word
    global zh_pattern
    return zh_pattern.search(word)

def contain_en(word):
    if word is None:
        return False
    word = word.decode()
    global en_pattern
    return en_pattern.search(word)

if __name__ == '__main__':

    print(my_split("abcgaggch", ["a", "c"]))

    # --------------------

    word1 = 'ceshi,测试'
    word2 = 'ceshi,ceshi'

    if contain_zh(word1):
        print('%s 里面有中文' % word1)
    if contain_zh(word2):
        print('%s 里面有中文' % word2)

# https://segmentfault.com/a/1190000006197218
def FullToHalf(s):
    n = []
    s = s.decode('utf-8')
    for char in s:
        num = ord(char)
        if num == 0x3000:
            num = 32
        elif 0xFF01 <= num <= 0xFF5E:
            num -= 0xfee0
        num = unichr(num)
        n.append(num)
    return ''.join(n)
'''
题目：
    在一个字符串（0<=字符串长度<=10000，全部由字母组成）中找到第一个只出现一次的字符，
    并返回它的位置，如果没有则返回-1（需要区分大小写）
'''


def FirstNotRepeatingChar(s):
    if s == '':
        return -1
    for i in s:
        if s.count(i) == 1:
            return i, s.index(i)

a = input("输入一个字符串：")
m, n = FirstNotRepeatingChar(a)
print('第一个出现一次的字符是：'+str(m)+' 位置是：'+str(n))
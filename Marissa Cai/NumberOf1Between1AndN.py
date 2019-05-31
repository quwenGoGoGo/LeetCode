'''
题目：
    输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数
    例如：输入12，从1到12这些整数中包含1的数字有1，10，11，12，1一共出现了5次
'''

'''
解析:
    考虑简单的一位数1-9；二位数10-99；三位数100-999：
    一位数：1-9中，1出现了1次   记为f(1)
    二位数：10-99中，对于十位数字一共出现了10次；对于个位数字，把数字分段分成10-19，20-29等等，
           那么一共分成9段，每一段上1出现的次数为1-9中1出现的次数，共出现次数f(1)*9+10*1
    三位数：100-999中，百位数字上一共出现了100次，即10**2；低位（除了百位数字）上分段100-199，200-299，
           300-399分成9段，一共出现次数9*f(2)+10**2
'''


# def get_1_digits(n):
#     '''
#     获取每个位数之间1的总数
#     :param n: 位数
#     :return:
#     '''
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     current = 9 * get_1_digits(n-1) + 10 ** (n-1)
#     return get_1_digits(n-1) + current
#
#
# def get_1_nums(n):
#     if n < 10:
#         return 1 if n >= 1 else 0
#     digit = get_digits(n)  # 位数
#     low_nums = get_1_digits(digit-1)  # 最高位之前的1的个数
#     high = int(str(n)[0])  # 最高位
#     low = n - high * 10 ** (digit-1)  # 低位
#
#     if high == 1:
#         high_nums = low + 1  # 最高位上1的个数
#         all_nums = high_nums
#     else:
#         high_nums = 10 ** (digit -1)
#         all_nums = high_nums + low_nums * (high - 1)  # 最高位大于1的话，统计每个多位数后面包含的1
#     return low_nums + all_nums + get_1_nums(low)
#
#
# def get_digits(n):
#     ret = 0
#     while n:
#         ret += 1
#         n /= 10
#     return ret
#
#
# def test_n(num):
#     # 常规方法用来比较
#     ret = 0
#     for n in range(1, num+1):
#         for s in str(n):
#             if s == '1':
#                 ret += 1
#     return ret
#
# if __name__ == '__main__':
#     test = 9923446
#     import time
#     t = time.clock()
#     print(test_n(test))
#     print(time.clock() - t)
#     t1 = time.clock()
#     print(get_1_nums(test))
#     print(time.clock() - t1)


def NumberOf1Between1AndN(n):
    mult, sumTimes = 1, 0
    while n // mult > 0:
        high, mod = divmod(n, mult * 10)
        curNum, low = divmod(mod, mult)
        if curNum > 1:
            sumTimes += high * mult + mult
        elif curNum == 1:
            sumTimes += high * mult + low + 1
        else:
            sumTimes += high * mult
        mult = mult * 10
    return sumTimes


a = int(input('输入一个数：'))
print(NumberOf1Between1AndN(a))


# 求整数中X的个数
def NumberOfXBetween1AndN(n, x):
    mult, sumTimes = 1, 0
    while n//mult > 0:
        high, mod = divmod(n, mult*10)
        curNum, low = divmod(mod, mult)
        if curNum > x:
            sumTimes += high*mult + mult
        elif curNum == x:
            sumTimes += high*mult + low + 1
        else:
            sumTimes += high*mult
        mult = mult * 10
    return sumTimes
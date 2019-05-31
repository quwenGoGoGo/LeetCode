'''
题目：
    丑数：只包含质因子2、3和5的数
    例如6、8都是丑数，但14不是，因为它包含质因子7
    习惯上我们把1当作是第一个丑数，求按从小到大的顺序的第N个丑数
'''

'''
思考：
    假设已有n个丑数，按照顺序排列，令第n个丑数为M，那么第n+1个丑数就是由这n个丑数
    分别乘以2，3，5，得到的所有大于M的结果中，最小的那个数。
    继续简化思路：事实上，我们不需要每次都计算前面所有的丑数乘以2，3，5，然后再比
    较大小。因为已经存在丑数中，一定存在某个数T2，在这个数之前的所有数乘以2都小于
    M，但是T2乘以2的结果一定大于M；同理，T3*3>M T5*5>M
'''
def GetUglyNumber(index):
    if index == 0:
        return 0
    # 1作为特殊数直接保存
    baselist = [1]
    # T2,T3,T5的初始索引值
    min2 = min3 = min5 = 0
    curnum = 1
    while curnum < index:
        minnum = min(baselist[min2]*2, baselist[min3]*3, baselist[min5]*5)
        baselist.append(minnum)
        # 找到T2，也就是判断T2*2>minnum
        while baselist[min2] * 2 <= minnum:
            min2 += 1
        # 找到T3
        while baselist[min3] * 3 <= minnum:
            min3 += 1
        # 找到T5
        while baselist[min5] * 5 <= minnum:
            min5 += 1
        curnum += 1
    return baselist[-1]

a = int(input("请输入需要的第几个丑数："))
print(GetUglyNumber(a))

'''
题目：
    计算连续子向量的最大和，当向量全为正数的时候好解决
    本题是建立在向量中有负数的情况下的，期望旁边的正数弥补它
    如：{6，-3，-2，7，-15，1，2，2}，连续子向量的最大和为8（第0个到第3个）
    给一个数组，返回它的最大连续子序列的和
'''

'''
思考：
    不考虑暴力搜索的方法
    定义两个变量，一个用来存储之前的累加值，一个用来存储当前的最大和，遍历数组中的每个元素，假设遍历到第i个数时：
    1.如果前面的累加值为负数或者等于0，那对累加值清0重新累加，把当前数的值赋给累加值；
    2.如果前面的累加值为正数，那么继续累加，即之前的累加值加上当前数的值作为新的累加值
    判断累加值是否大于最大值：如果大于最大值，则最大和更新，否则，继续保留之前的累加和
'''

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        sum = array[0]
        presum = 0
        l = len(array)
        for i in range(l):
            if presum < 0:
                presum = array[i]
            else:
                presum += array[i]
            sum = max(sum, presum)
        return sum

s = Solution()
A = [int(n) for n in input("输入一个数组：").split()]
print("最大连续子向量为：", s.FindGreatestSumOfSubArray(A))


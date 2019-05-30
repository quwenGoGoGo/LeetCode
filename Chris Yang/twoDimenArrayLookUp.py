'''
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''


import numpy as np

class Solution:
    def Find(self,target,array):
        rows = array.shape[0]
        cols = array.shape[1]
        if rows>0 and cols>0:
            row = 0; col = cols -1
            while row<rows and col>=0:
                if array[row,col] == target:
                    print([row,col])
                    return True
                elif array[row,col] <target:
                    row+=1
                else:
                    col-=1
            return False
        return False

if __name__ == '__main__':
    array = np.array([range(i,i+3) for i in [2,5,8]])
    target = Solution().Find(7,array)
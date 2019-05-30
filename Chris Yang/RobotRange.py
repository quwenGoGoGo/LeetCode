'''
题目描述:
        地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
    每一次只能向左，右，上，下四个方向移动一格，
    但是不能进入行坐标和列坐标的数位之和大于k的格子。
    例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
    但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
    请问该机器人能够达到多少个格子？
'''

import numpy as np
from functools import reduce

class Solution:
    def movingCount(self,threshold,rows,cols):
        chess = np.zeros((rows, cols))
        return self.move2next(chess,0,0,rows,cols,threshold)


    def move2next(self,chess,row,col,rows,cols,threshold):
        count = 0
        # if row >= rows or col >= cols or row < 0 or col < 0 or chess[row,col] == 1:
        #     return count
        # sum = reduce(lambda x, y: x + y, num2str(row) + num2str(col))
        # if sum > threshold:
        #     return count
        # else:
        if row <rows and col <cols and row >= 0  and col >= 0  and chess[row,col] != 1 and (reduce(lambda x, y: x + y, num2str(row) + num2str(col))) <= threshold:
            chess[row,col] = 1
            count=1+self.move2next(chess, row, col + 1, rows, cols, threshold)\
                  +self.move2next(chess, row, col - 1, rows, cols, threshold)+\
                  self.move2next(chess, row - 1, col, rows, cols, threshold)+\
                  self.move2next(chess, row + 1, col + 1, rows, cols, threshold)
        return count


def num2str(value):
    a = list(map(int,str(value)))
    return a

if __name__ == '__main__':
    a = Solution()
    b = a.movingCount(6,5,5)
    print(b)
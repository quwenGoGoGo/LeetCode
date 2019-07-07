"""
-------------------------------------------------
   File Name：       Balanced binary tree
   Description:
   Author:           Marisa
   date：            2019/07/07
-------------------------------------------------
   Change Activity:  2019/07/07
-------------------------------------------------
"""
__author__ = 'Marisa'

def IsBalanced_Solution(pRoot):
    def height(node):
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        return max(left, right) + 1
    return height(pRoot) != -1
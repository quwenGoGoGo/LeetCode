'''
题目：
    找到二叉树的深度
'''
'''
思考：
    递归的思路，二叉树的每个结点可以看作是"根结点"，对于根结点，求这个根结点的最大深度，
    那么就求出这个根结点的左右子树的深度，max比较最大的再加一；对于左右子树的，同样对
    根结点求左右子树的深度...直到叶子结点，它没有左右子树，那么它的最大深度直接赋为1，
    然后一层一层往上去实现，刚刚是从根结点往叶子结点实现，这样就可以求出根结点到叶子结点的
    最大深度
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def TreeDepth(pRoot):
    if pRoot == None:
        return 0
    lDepth = TreeDepth(pRoot.left)
    rDepth = TreeDepth(pRoot.right)
    return max(lDepth, rDepth) + 1
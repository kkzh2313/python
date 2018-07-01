'''
题目描述
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if not root.left and not root.right and expectNumber == root.val:
            return [[root.val]]
        result = []
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)
        for i in left + right:
            result.append([root.val] + i)
        return result
#######方法2需要重新改进一直有错误


class Solution2:


    def FindPath(self, root, expectNumber):
        # listAll = [[]]
        # list = []
        if not root:
            return listAll
        list.extend([root.val])
        a=list
        expectNumber -= root.val

        if expectNumber==0 and (not root.left) and (not root.right):
            listAll.append(list)
        self.FindPath(root.left,expectNumber)
        self.FindPath(root.right,expectNumber)
        list.pop()
        return listAll

pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)
listAll = [[]]
list = []

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5


S = Solution2()

print(S.FindPath(pNode1, 22))
# 测试用例：[1,-2,-3,1,3,-2,null,-1]  -1
# 测试用例：[-2, None, -3] -5
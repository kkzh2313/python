'''题目描述
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。' \
'''

'''
利用递归实现。如果一棵树只有一个结点，那么它的深度为1。
递归的时候无需判断左右子树是否存在，因为如果该节点为叶节点，它的左右子树不存在，那么在下一级递归的时候，直接return 0。
同时，记得每次递归返回值的时候，深度加一操作。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 递归解法, 简单直接, 时间复杂度O(n), 空间复杂度O(logn)
    def TreeDepth(self, pRoot):
        if pRoot == None :
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left,right)+1
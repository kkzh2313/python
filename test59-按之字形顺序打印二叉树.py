'''
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 存储点的时候按照奇数层和偶数层分别存储
    def Print(self, pRoot):
        if pRoot == None:
            return []
        nodes = [pRoot]
        result =[]
        lefttoright = True  #奇数行从左往右读出 标志为True,偶数行则倒转
        while nodes:
            cur , next = [],[]
            for i in nodes:
                cur.append(i.val)
                if i.left:
                    next.append(i.left)
                if i.right:
                    next.append(i.right)
            if lefttoright == False:
                cur.reverse()
            result.append(cur)
            nodes = next
            lefttoright = not lefttoright #读取一行切换状态，因为奇数偶数行切换
        return result

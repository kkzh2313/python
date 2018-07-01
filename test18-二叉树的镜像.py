'''题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
'''



# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''方法一、递归的思路'''
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:#kongshu
            return root
        # if root.left == None and root.right == None:#单节点树
        #         #     return
        root.left,root.right = root.right,root.left
        if root.left: #左子树不为空就继续递归镜像左子树
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
#上面不加两个if也可以，只是在单边树的情况多次执行无用的函数浪费时间
pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)


pNode1.left = pNode2
pNode1.right = pNode3

pNode2.left = pNode4
pNode2.right = pNode5

pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
S.Mirror2(pNode1)

print(pNode1.right.left.val)
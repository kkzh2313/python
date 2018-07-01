'''
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
'''
思路：层次遍历也就是广度优先遍历，用到队列
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = [root]#定义一个队列用来存放树的各层元素
        result = [] #result列表用来保存层次遍历的结果
        while queue:
            currentRoot = queue.pop(0) #当前根节点是队列queue的第一个元素，也是需要将其val值添加到result结果列表最后
            result.append(currentRoot.val)
            if currentRoot.left: #当前结点的左结点存在就从队列后面进入
                queue.append(currentRoot.left)
            if currentRoot.right:#当前结点的右结点存在就从队列后面进入
                queue.append(currentRoot.right)
        return result
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
print(S.PrintFromTopToBottom(pNode1))
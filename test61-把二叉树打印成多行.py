'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''
'''
引入两个队列。首先把当前层的节点存入到一个队列queue1中，然后遍历当前队列queue1，
在遍历的过程中，如果节点有左子树或右子树，依次存入另一个队列queue2。
然后遍历队列queue2，如此往复。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def levelOrder(self, pRoot):
        if  not pRoot:
            return []
        nodes,result = [pRoot],[] #定义两个数组，一个是当前行结点的保存数组，一个是最终的结果输出数组
        #如果当前行不为空就一直遍历下去
        while nodes:
            curQueue , nextQueue = [],[] #定义两个队列数组，一个保存当前行各结点的值，一个保存当前行各结点的子节点

            for i in nodes:  #遍历当前行，进行保存结点值（到cur数组）、读取结点的子节点（到next数组）操作
                curQueue.append(i.val)
                if i.left:
                    nextQueue.append(i.left)
                if i.right:
                    nextQueue.append(i.right)
            result.append(curQueue)
            nodes = nextQueue  #重置当前行结点 数组
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
aList = S.levelOrder(pNode1)
print(aList)
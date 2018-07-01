'''
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

'''
递归版
解题思路：
1.将左子树构造成双链表，并返回链表头节点。
2.定位至左子树双链表最后一个节点。
3.如果左子树链表不为空的话，将当前root追加到左子树链表。
4.将右子树构造成双链表，并返回链表头节点。
5.如果右子树链表不为空的话，将该链表追加到root节点之后。
6.根据左子树链表是否为空确定返回的节点。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree == None: #空树
            return None
        if pRootOfTree.left == None and pRootOfTree.right ==None: #单节点数
            return pRootOfTree
        #第一步处理左子树
        self.Convert(pRootOfTree.left)

        #第二步连接左子树最大节点与根节点
        left = pRootOfTree.left
        if left:#当左子树存在时，循环往下找‘左’子树的右节点就是该左子树最大的节点
            while left.right:
                left = left.right
            pRootOfTree.left,left.right = left, pRootOfTree

        #第三步处理右子树
        self.Convert(pRootOfTree.right)
        #第四步 连接右子树最小节点与根节点
        right = pRootOfTree.right
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree

        #第五步找到双向链表的头节点，也就是二叉树的最左子树左节点
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree
        self.left = None
        self.right = None

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
newList = S.Convert(pNode1)
print(newList.val)
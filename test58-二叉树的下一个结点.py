'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

'''

shu上思路
我们可发现分成两大类：
1、有右子树的，那么下个结点就是右子树最左边的点；
2、没有右子树的，也可以分成两类，
        a)是父节点左孩子 ，那么父节点就是下一个节点 ； 
        b)是父节点的右孩子，找他的父节点的父节点的父节点...
        直到当前结点是其父节点的左孩子位置。如果没有eg：M，如果有，其父节点就是尾节点。

'''
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode == None:
            return None
        #请况1 如果该结点有右节点
        if pNode.right != None :
            pNode = pNode.right
            while pNode.left!=None:
                pNode = pNode.left
            return pNode
        #情况2 该节点没有右节点
        #没右子树，则找第一个当前节点是父节点左孩子的节点
        while pNode.next != None:
            if pNode == pNode.next.left:
                return pNode.next
            pNode = pNode.next
        return None #退到了根节点仍没找到，则返回nul

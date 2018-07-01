'''
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
'''
思路：
1. 把复制的结点链接在原始链表的每一对应结点后面 
2. 把复制的结点的random指针指向被复制结点的random指针的下一个结点
3. 拆分成两个链表，奇数位置为原链表，偶数位置为复制链表，
注意复制链表的最后一个结点的next指针不能跟原链表指向同一个空结点None，
next指针要重新赋值None(判定程序会认定你没有完成复制）
'''
# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    # 每一步输入头结点，内部操作在每一步具体函数中已完成，
    #结点的一些定义需要每一步再重新定义
    def Clone(self, pHead):
        if pHead == None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)
    #第一步复制结点
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.label = pNode.label
            pCloned.next = pNode.next

            pNode.next = pCloned
            pNode = pCloned.next

    # 第二步建立random结点，将复制后的链表中的复制结点的random指针链接到被复制结点random指针的后一个结点
    def ConnectRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random != None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    # 第三步拆分链表, 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pClonedHead = pHead.next #保存一个复制链表的头结点

        while pNode:
            pClonedNode = pNode.next #定义复制点是当前原结点的下一个结点
            pNode_next = pClonedNode.next #定义复制点的下一个点是原链表当前结点的下一个节点
            pNode.next = pNode_next
            if pNode_next:#若当前原结点的下一原节点存在
                pClonedNode.next = pNode_next.next
            else:
                pClonedNode.next = None

            pNode = pNode.next #将当前结点更正
        return pClonedHead









def ReconnectNodes(self, pHead):
    pNode = pHead
    pClonedHead = pHead.next
    while pNode:
        pClonedNode = pNode.next
        pNode.next = pClonedNode.next

        if pClonedNode.next:
            pClonedNode.next = pClonedNode.next.next
        else:
            pClonedNode.next = None

        pNode = pnodenext

'''
不通过
您的代码已保存
答案错误:您提交的程序没有通过所有的测试用例
case通过率为0.00%

测试用例:
{1,2,3,4,5,3,5,#,2,#}

对应输出应该为:

{1,2,3,4,5,3,5,#,2,#}

你的输出为:

'NoneType' object has no attribute 'next'
'''

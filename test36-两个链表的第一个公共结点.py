'''
题目描述
输入两个链表，找出它们的第一个公共结点。
'''

'''
首先依次遍历两个链表，记录两个链表的长度m和n，如果 m > n，
那么我们就先让长度为m的链表走m-n个结点，然后两个链表同时遍历，
当遍历到相同的结点的时候停止即可。对于 m < n，同理。'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 == None or pHead2 == None:
            return None
        #首先获取两个链表的长度，
        nLength1 = self.GetListLength(pHead1)
        nLength2 = self.GetListLength(pHead2)
        nlengthDif = abs(nLength1-nLength2)
        #确定最长、最短链表头结点
        if nLength1 > nLength2:
            pHeadLong = pHead1
            pHeadShort = pHead2
        else:
            pHeadLong = pHead2
            pHeadShort = pHead1
        for i in range(nlengthDif):
            pHeadLong = pHeadLong.next
        # while pHeadLong != None and pHeadShort != None and pHeadLong.val != pHeadShort.val:
        while pHeadLong != None and pHeadShort != None and pHeadLong != pHeadShort:
            pHeadLong = pHeadLong.next
            pHeadShort =pHeadShort.next
        pFirstCommonNode = pHeadLong
        return pFirstCommonNode

    def GetListLength(self,pHead):
        length = 0
        while pHead:
            pHead = pHead.next
            length += 1
        return length

'''
最短的代码，不用记长度
用两个指针扫描”两个链表“，最终两个指针到达 null 或者到达公共结点

长度相同有公共结点，第一次就遍历到；没有公共结点，走到尾部NULL相遇，返回NULL
长度不同有公共结点，第一遍差值就出来了，第二遍一起到公共结点；没有公共，一起到结尾NULL。

有环的话不行
'''
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            if p1 == None:
                p1 = pHead2
            else :
                p1 =p1.next
            if p2 == None:
                p2 = pHead1
            else :
                p2 = p2.next
        return p1


#构建第一个链表
node11 = ListNode(1)
node12 = ListNode(2)
node13 = ListNode(5)
node14 = ListNode(6)
node11.next = node12
node12.next = node13
node13.next = node14
#构建第二个链表
node21 = ListNode(11)
node22 = node13
node23 =
node4.next = node6


s = Solution()
result = s.FindFirstCommonNode(node1,node4)
print(result)


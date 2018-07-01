'''

题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#################递归版本
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pMerged = None #定义合并后链表的头结点
        #开始分析考虑特殊情况
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        else:                  #普通情况下，依次判断当前的结点谁最小，小的放到合并链表。接下来递归递归调用函数
            if pHead1.val <pHead2.val:
                pMerged = pHead1
                pMerged.next = self.Merge(pHead1.next,pHead2)
            else:
                pMerged = pHead2
                pMerged.next = self.Merge(pHead1,pHead2.next)
            return pMerged

###非递归版本
class Solution2:
    def Merge(self,pHead1,pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        #定义两个新结点，pMerged保存合并链表最初的结点，pNew是作为合并链表每次更新的当前新结点
        pMerged = None
        pNew = None
        while(pHead1 and pHead2 ):
            if pHead1.val < pHead2.val:
                if pMerged == None:
                    pMerged = pNew = pHead1
                else:
                    pNew.next = pHead1
                    pNew = pNew.next
                pHead1 = pHead1.next
            else:
                if pMerged == None:
                    pMerged = pNew =pHead2
                else:
                    pNew.next = pHead2
                    pNew = pNew.next
                pHead2 = pHead2.next
        if pHead1 is None:
            pNew.next = pHead2
        if pHead2 is None :
            pNew.next = pHead1
        return pMerged





node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(4)

node6 = ListNode(6)
node4.next = node6


s = Solution2()
merge_ll=s.Merge(node1,node4)
while merge_ll: #打印合并的链表，查看结果对不对
    print(merge_ll.val)
    merge_ll = merge_ll.next



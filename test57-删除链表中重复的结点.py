'''
删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点
#-*- coding:utf-8 -*-
class ListNode:，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''
##########建立一个新建头结点 ，防止链表的头结点是重复的删除掉

    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self,pHead):
        #定义一个新的头结点，避免首节点就是重复的被删
        first = ListNode(0)
        first.next = pHead  #新建头结点 后接链表的原头结点
        p = pHead  #p用来遍历链表所有结点时的一个结点符
        last = first  # last 用来遍历除去重复结点余下结点的  结点符
        #开始遍历整个链表
        while p != None and p.next != None:
            if p.val == p.next.val:
                val = p.val
                while p!=None and p.val == val:
                    p = p.next
                last.next = p
            else:
                last = p
                p = p.next
        return first.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
p = s.deleteDuplication(node1)
while p is not None:
    print(p.val)
    p = p.next
# for i in
# print(s.deleteDuplication(node1).next.next.val)

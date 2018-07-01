'''
15/题目描述
输入一个链表，反转链表后，输出链表的所有元素。
'''

'''
思路：定义两个变量，分别保存前指针和后指针。'''
# 当前节点是pHead， Pre为当前节点的前⼀节点， Next为当前节点的下⼀节点
# 需要pre和next的⽬的是让当前节点从pre->head->next1->next2变成pre<-head next1->next2
# 即pre让节点可以反转所指⽅向，但反转之后如果不⽤next节点保存next1节点的话，此单链
#表就此断开了
# 所以需要⽤到pre和next两个节点
# 1->2->3->4->5
# 1<-2<-3 4->5
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):#pHead指当前结点，Pre为前一结点，Next为后一节点
        # write code here
        if pHead == None :
            return None
        Pre = None
        Next = None
        while pHead != None:
            Next = pHead.next #先用next保存phead的下一个节点的信息，保证单链表不会因为失去head节点的原next节点而就此断裂
            pHead.next = Pre  #保存完next，就可以让phead从指向next变成指向pre了，

#/让pre，phead，next依次向后移动一个节点，继续下一次的指针反转
            Pre = pHead
            pHead = Next
        return Pre



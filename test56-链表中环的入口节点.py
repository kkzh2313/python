'''
一个链表中包含环，请找出该链表的环的入口结点。
'''



'''
此问题包含两个步骤：

（1）判断链表中是否有环

（2）找出环

一、

1）选择快慢指针，让快指针每次走两步，慢指针每次走一步，
若是单链表中有环的话，那么两个指针会相遇，即指向的相同的节点的值相等来判断。

2）当相遇的时候，慢指针在环中走了k步，设环之外的部分长为x,环的长度为n,则快指针一共走了 x+m*n步，（m为快指针在环中走的圈数），
慢指针一共走了x+k步，因为快指针的速度是慢指针的两倍。那么可以得到2(x+k)=x+m*n+k;得到x为m*n-k ,慢指针在圈中还剩下的步数n-k;

二、

让快指针从头开始，两个指针每次都走一步，当快指针走了x=(m*n-k)步的时候，到达环的入口，慢指针在圈中走m-1圈加n-k步的时候，
也到达环入口那个节点，两个指针再次相遇，此刻的节点就是环的入口的节点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def MeetingNode(self, pHead):
        if pHead == None or pHead.next == None:
            return None
        pslow =pfast = pHead
        while pslow != None and pfast != None:
            pslow = pslow.next
            pfast = pfast.next.next #快指针每次跑两步
            #找到相遇点，重置快节点，两者同步跑，直到相遇
            if pslow == pfast:
                pfast = pHead
                while pfast!=pslow:
                    pslow = pslow.next
                    pfast = pfast.next

                return pslow
        #遍历完发现没有环
        return None




node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.MeetingNode(node1).val)


def EntryNodeOfLoop(self, pHead):
    # write code here
    p = q = pHead
    while q != None and q.next != None:
        p = p.next
        q = q.next.next
        if p == q:
            q = pHead
            while p != q:
                q = q.next
                p = p.next
            if p == q:
                return p
    return None
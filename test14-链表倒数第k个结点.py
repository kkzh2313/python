'''
题目描述
输入一个链表，输出该链表中倒数第k个结点。

'''

'''
代码的鲁棒性。需要注意：如果输入的链表为空；k大于链表的长度；k为0的情况。
对于正常情况，设置两个指针分别指向头结点，第一个指针向前走k-1步，走到正数第k个结点，同时保持第二个指针不动，
然后第一个指针和第二个指针每次同时前移一步，这样第一个指针指向尾结点的时候，第二个指针指向倒数第k个结点。
判断尾结点的条件是 pNode.next == None

推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,
  快指针指到尾部, 慢指针正好指到中间

'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        tmp = head
        count =0  #count是保存链表的长度，初始为0
        while tmp:
            tmp = tmp.next
            count += 1
        if count<k or k<0 or head==None:#链表不够k的长度，或k小于0，或链表为空，为特殊情况
            return 0
        p = head #第一个指针p，跑在前面
        q = head #定义第二个指针，跑在后面
        for i in range(k):#diyige指针领先k-1个结点
            p = p.next
        while p:
            p = p.next
            q =q.next
        return q.val
h = ListNode(None)
node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3
h.next = node1
s = Solution()
print(s.FindKthToTail(h,4))
'''
方法二：
个⼈总结最佳算法，先计算链表的⻓度，然后计算找到倒数第k个需要⼏次循环，并判断其
中关系。最后⽤for循环，不断将指针指向下⼀个节点，即为所求。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution2:
    def FindKthToTail(self, head, k):
        tmp = head
        len_node = 0
        while tmp:
            tmp=tmp.next
            len_node += 1
        runtime = len_node - k
        node = head
        if runtime<0 or k<0 :#ruguo k比链表长或者k小于0，为特殊条件
            return 0
        else:
            for i in range(runtime)：
                node = node.next
            return node.val



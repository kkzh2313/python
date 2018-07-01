#输入一个链表，从尾到头打印链表每个节点的值。
class Listnode:
    def __init__(self,x=None):
        self.val=x
        self.next=None

class Solution:
    def printListFromTailToHead(self,listnode):
        if listnode.val == None:
            return None
        l=[]
        head=listnode
        while head :
            l.insert(0,head.val)      ####insert方法将数值插入给定的位置
            head=head.next
        return l
node1=Listnode(10)
node2=Listnode(11)
node3 = Listnode(13)
node1.next = node2
node2.next = node3

singleNode = Listnode(12)

test = Listnode()

S = Solution()
print(S.printListFromTailToHead(node1))
print(S.printListFromTailToHead(test))
print(S.printListFromTailToHead(singleNode))
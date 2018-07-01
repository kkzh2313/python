'''
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

'''
基于二叉树的深度，再次进行递归。
以此判断左子树的高度和右子树的高度差是否大于1，若是则不平衡，反之平衡。
'''
#这种方法存在重复遍历节点的问题
class Solution2:
    def getDepth(self, pRoot):
        if pRoot == None:
            return 0
        return max(self.getDepth(pRoot.left), self.getDepth(pRoot.right)) + 1
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        if abs(self.getDepth(pRoot.left)-self.getDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)



#xiamian方法避免了一个节点被重复遍历多次
# 借用后序遍历的方式遍历二叉树的每个节点，那么遍历到一个节点之前我们已经遍历了它的左子树 右子树
#只要在遍历每个节点的时候记录它的深度，就可以一边遍历一边判断每个节点是不是平衡的
'''这里flag初始条件有啥区别'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.flag = True #flag初始为True，后面只要一个子树为非平衡树就是FALSE

    def IsBalanced_Solution(self, pRoot):
        self.GetDepth(pRoot)
        return self.flag

    def GetDepth(self,pRoot):
        if pRoot == None:
            return 0
        left = 1+self.GetDepth(pRoot.left)
        right = 1+self.GetDepth(pRoot.right)
        # 下面的呢段代码可简化只判断flag为FALSE情况，因为只要一段子树不是平衡的，那整体就是非平衡树
        # if abs(left-right)<=1:
        #     self.flag = True
        # else :
        #     self.flag = False
        if abs(left-right)>1:
            self.flag = False
        return left if left>right else right #返回左右子树中深度最大的  或者 max(left,right)

# pNode1 = TreeNode(1)
# pNode2 = TreeNode(2)
# pNode3 = TreeNode(3)
# pNode4 = TreeNode(4)
# pNode5 = TreeNode(5)
# pNode6 = TreeNode(6)
# pNode7 = TreeNode(7)
#
# pNode1.left = pNode2
# pNode1.right = pNode3
# pNode2.left = pNode4
# pNode2.right = pNode5
# pNode3.right = pNode6
# pNode5.left = pNode7

pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode5.left = pNode6

s= Solution()
print(s.GetDepth(pNode1))
print(s.IsBalanced_Solution(pNode1))
#注意输入空树{}，也是平衡树返回True
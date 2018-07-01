'''
##########重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
则重建二叉树并返回。
'''
class  TreeNode:
    def __init__(self,x):
        self.val=x
        self.left= None
        self.right=None
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        if set(pre)!=set(tin):  #两个序列中数字有不同的
            return None

        i=tin.index(pre[0])  #根节点的位置在中序遍历中
        root = TreeNode(pre[0])
        root.left=self.reConstructBinaryTree(pre[1:i+1],tin[0:i])
        root.right=self.reConstructBinaryTree(pre[i+1:],tin[i+1:])
        return root
pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
test=Solution()
newtree=test.reConstructBinaryTree(pre,tin)
'''
postorder=[]
while newtree:
    postorder.append(item)

print (newtree)
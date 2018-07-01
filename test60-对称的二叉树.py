'''
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''


''''
/*思路：首先根节点以及其左右子树，左子树的左子树和右子树的右子树相同
* 左子树的右子树和右子树的左子树相同即可，采用递归

* 非递归也可，采用栈或队列存取各级子树根节点.引入两个队列。
首先把当前层的节点存入到一个队列queue1中，然后遍历当前队列queue1，在遍历的过程中，
如果节点有左子树或右子树，依次存入另一个队列queue2。然后遍历队列queue2，如此往复。

二叉树是否对称，只要采用前序、中序、后序、层次遍历等任何一种遍历方法，分为先左后右和先
右后左两种方法，只要两次结果相等就说明这棵树是一颗对称二叉树。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归方法1
class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot == None:
            return True
        return self.selfIsSymmetrical(pRoot.left,pRoot.right)

    def selfIsSymmetrical(self,lRoot,rRoot):
        if lRoot == None and rRoot == None:
            return True
        if lRoot != None and rRoot != None:
            return lRoot.val == rRoot.val and self.selfIsSymmetrical(lRoot.left,rRoot.right) and self.selfIsSymmetrical(lRoot.right,rRoot.left)
        return False
#递归方法2
class Solution2:
    def isSymmetrical(self, pRoot):
         return self.selfIsSymmetrical(pRoot, pRoot)
    def selfIsSymmetrical(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 == None:  #因为上面条件中root1 和root2全为空了，所以这里肯定不会全部为空
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.selfIsSymmetrical(pRoot1.left, pRoot2.right) and self.selfIsSymmetrical(pRoot1.right, pRoot2.left)

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
result = S.isSymmetrical(pNode1)
print(result)
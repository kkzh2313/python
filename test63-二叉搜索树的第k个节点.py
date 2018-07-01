# -*- coding:utf-8 -*-
'''
给定一颗二叉搜索树，请找出其中的第k大的结点。例如，
    5
   / \
  3  7
 /\ /\
2 4 6 8 中，
按结点数值大小顺序第三个结点的值为4。
'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.treeNode = []

    def inOrder(self, pRoot):
        if len(self.treeNode) < 0:
            return None
        if pRoot.left:
            self.inOrder(pRoot.left)
        self.treeNode.append(pRoot)
        if pRoot.right:
            self.inOrder(pRoot.right)

    def KthNode(self, pRoot, k):
        if k == 0 or pRoot == None:
            return
        self.inOrder(pRoot)
        if len(self.treeNode) < k:
            return None
        return self.treeNode[k - 1]
        


class Solution1:
    def __init__(self):
        self.index = 0
    def KthNode(self,pRoot,k):
        if pRoot == None:
            return None
        node = self.KthNode(pRoot.left,k)
        if node != None:
            return node
        self.index += 1
        if self.index == k:
            return pRoot
        node = self.KthNode(pRoot.right,k)
        if node != None:
            return node
class Solution1:
    def __init__(self):
        self.index = 0
    def KthNode(self,pRoot,k):
        if pRoot != None:
            node = self.KthNode(pRoot.left,k)
            if node != None: #返回递归找到的该节点
                return node
            self.index += 1
            if self.index == k: #找到所求的第k个节点，递归结束
                return pRoot
            node = self.KthNode(pRoot.right,k)
            if node != None:#返回递归找到的该节点
                return node
        return None
#######调试版本----------
class Solution2:
    def __init__(self):
        self.index = 0
        self.c1 = 0
        self.c2 = 0
    def KthNode(self,pRoot,k):

        if pRoot == None:
            return None,-1

        rootVal = pRoot.val
        self.c1 += 1
        ceng = self.c1
        node, value = self.KthNode(pRoot.left,k)
        if node != None:
            return node , node.val
        self.index += 1
        if self.index == k:
            return pRoot,pRoot.val
        node, value = self.KthNode(pRoot.right,k)
        if node != None:
            return node,node.val
        else:
            return None,-1




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

#
# S = Solution1()
# aList = S.KthNode(pNode1,5)
# print(aList.val)

S = Solution2()
aList,resultVal = S.KthNode(pNode1,4)
print(aList,resultVal)


'''      
链接：https://www.nowcoder.com/questionTerminal/ef068f602dde4d28aab2b210e859150a
来源：牛客网   高赞回答哈哈

//思路：二叉搜索树按照中序遍历的顺序打印出来正好就是排序好的顺序。
//     所以，按照中序遍历顺序找到第k个结点就是结果。
public class Solution {
   int index = 0; //计数器
    TreeNode KthNode(TreeNode root, int k)
    {
        if(root != null){ //中序遍历寻找第k个
            TreeNode node = KthNode(root.left,k);
            if(node != null)
                return node;
            index ++;
            if(index == k)
                return root;
            node = KthNode(root.right,k);
            if(node != null)
                return node;
        }
        return null;
    }
}
'''
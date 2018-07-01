
'''
请实现两个函数，分别用来序列化和反序列化二叉树。这里没有规定序列化的方式。
'''

'''首先来看二叉树的序列化，二叉树的序列化就是采用前序遍历二叉树输出节点，
再碰到左子节点或者右子节点为None的时候输出一个特殊字符”#”。
对于反序列化，就是针对输入的一个序列构建一棵二叉树，我们可以设置一个指针先指向序列的最开始，
然后把指针指向位置的数字转化为二叉树的结点，后移一个数字，继续转化为左子树和右子树。
当遇到当前指向的字符为特殊字符”#”或者指针超出了序列的长度，则返回None，
指针后移，继续遍历。'''

#用递归的思路

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.index = -1
    def Serialize(self, root):
        if not root:
            return '#,'
        return str(root.val)+',' + self.Serialize(root.left) +self.Serialize(root.right)
    def Deserialize(self, s):
        l = s.split(',')
        self.index += 1
        if self.index >= len(l) or l[self.index] == '#':
            return None
        # node = None
        node = TreeNode(int(l[self.index]))
        node.left = self.Deserialize(s)
        node.right = self.Deserialize(s)
        return node

if __name__ == '__main__':
    S = Solution()
    s = '8,6,10,5,7,9,11'
    strTree = S.Deserialize(s)   #反序列化成树
    print(S.Serialize(strTree))   #序列化结果







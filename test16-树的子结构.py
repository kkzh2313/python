'''
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''

'''
http://www.cnblogs.com/heyonggang/archive/2013/11/03/3405482.html
要查找树A中是否存在和树B结构一样的子树，可以分成两步：

1/第一步在树A中找到和B的根节点的值一样的结点R；------y用函数HasSubtree来表示
2/第二步再判断树A中以R为根结点的子树是不是包含和树B一样的结构。用函数IsSubtree（）表示

第一步在树A中查找与根结点的值一样的结点，这实际上就是树的遍历。递归调用HasSubTree遍历二叉树A。
如果发现某一结点的值和树B的头结点的值相同，则调用DoesTreeHavaTree2，做第二步判断。

第二步是判断树A中以R为根结点的子树是不是和树B具有相同的结构。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    # def HasSubtree(self, pRoot1, pRoot2): #pRoot2是要判断的子树结构
    #     if pRoot1 == None or pRoot2 == None:#如果树都是空的，则是错的
    #         return False
    #     result = False  # 定义默认结果为False
    #     #下面开始判断，三个遍历方向
    #     #1、当前结点值相等，就看
    #     if pRoot1.val == pRoot2.val:
    #         result = self.IsSubtree(pRoot1,pRoot2)
    #     if not result:
    #         result = self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
    #     # if not result:
    #     #     result = self.HasSubtree(pRoot1.right,pRoot2)
    #     return result
    '''
    函数1 的方法2
    '''
    def HasSubtree(self, pRoot1, pRoot2): #pRoot2是要判断的子树结构
        if pRoot1 == None or pRoot2 == None:
            return False
        #结点值相等就继续判断第二步；如果节点值不相等，就分别找1的左子树（右子树）结点值和树2结点是否相等。这三种情况中只要有一种情况是真就返回结果是真
        return self.IsSubtree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot)

    def IsSubtree(self,pRoot1,pRoot2):
        if pRoot2 == None:#子树2为空也就是进入到最深层后判断完quanbu
            return True
        if pRoot1 == None :#树一为空，表示树1判断完了，树2还没有判断完，那肯定表示2树不是1树的子结构
            return False
        if pRoot1.val == pRoot2.val:  #如果第2步里 首先是看当前结点的值是否相等，相等就看左右子树的值是否相等
            return self.IsSubtree(pRoot1.left,pRoot2.left) and self.IsSubtree(pRoot1.right,pRoot2.right)
        else:
            return False
#牛客网测试用例是层序遍历测试用例:
#{8,8,7,9,2,#,#,#,#,4,7},{8,9,2}

pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.HasSubtree(pRoot1, pRoot8))
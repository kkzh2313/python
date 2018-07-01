'''
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同
'''

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        length = len(sequence)
        root = sequence[-1]
        index = 0
        #遍历的范围是除最后一个根节点外前面的序列
        for i in range(length-1):
            index = i
            if sequence[i]>root:
                break
        ####注意这里是从index+1开始，因为默认sequence[index]>root,否则左子树这种会判错
        for j in range(index+1,length-1): 
            if sequence[j]<root:
                return False

        left = True
        if index > 0:
            return self.VerifySquenceOfBST(sequence[:i])

        right = True
        if index < length-1:
            return self.VerifySquenceOfBST(sequence[i:length-1])

        return  left and right

array = [5, 7, 6, 9, 11, 10, 8] #true
array2 = [4, 6, 7, 5] #true
array3 = [1, 2, 3, 4, 5]#zuozishu ---true
array4 = [6,7,8,9,5]#右子树 --true

S = Solution()
# print(S.VerifySquenceOfBST(array))
# print(S.VerifySquenceOfBST(array2))
print(S.VerifySquenceOfBST(array3))
# print(S.VerifySquenceOfBST(array4))

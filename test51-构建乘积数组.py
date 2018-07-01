'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1]
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''


'''
思路构建一个方阵 看出规律

剑指的思路：
B[i]的值可以看作下图的矩阵中每行的乘积。
下三角用连乘可以很容求得，上三角，从下向上也是连乘。
因此我们的思路就很清晰了，先算下三角中的连乘，即我们先算出B[i]中的一部分，然后倒过来按上三角中的分布规律，把另一部分也乘进去
'''
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if A == None or len(A)<1:
            return
        length = len(A)
        #B数组就是要求的，先在里面都放数字1
        B = [1]*length
        #先计算下三角的乘积值，从上往下
        for i in range(1,length):
            B[i] = B[i-1]*A[i-1]
        #再补充上上三角的计算，从下往上走
        temp = 1  # 这一变量保存上三角跑到某一行的值
        for i in range(length-2,-1,-1):
            temp *= A[i+1]
            B[i] *= temp
        return B
test = [1, 2, 3, 4]
s = Solution()
print(s.multiply(test))
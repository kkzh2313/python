'''
0, 1, 2, n-1这n个数字排成一个圆环, 从数字0开始每次从这个圆圈里删除第m个数字
求这个圆圈中最后剩下的一个数字
'''

'''递推公式：f[i] = (f[i-1]+m)%i n>1；当n=1 为0。  约瑟夫环问题
详情见书的创新方法或者博客https://blog.csdn.net/u012505432/article/details/51747181
'''
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        remain = 0
        for i in range(2,n+1):
            remain = (remain+m)%i
        return remain
s=Solution()
n=5
m=3
print(s.LastRemaining_Solution(n,m))

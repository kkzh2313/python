
'''
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

'''
清新的思路是：可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如 
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可。'''
#每次循环过程都是两步，
# 一、是将二维数组的第一行弹出保存
#二、对剩下的二维数组进行逆时针旋转
'''
reverse()，翻转列表元素
pop()弹出列表中的元素，默认是最后一个
+ 用于列表中，可以将元素添加到原列表后面'''

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = [] #这是存放最终的输出
        while matrix:
            # 每次都是将（最开始的/旋转后）二维数组的第一行弹出添加到结果列表后面
            result = result + matrix.pop(0)
            if not matrix or not matrix[0] : #进行到最后一步matrix为空，不需要进行下面的翻转了
                break
            matrix = self.turn(matrix)
        return result
    def turn(self,matrix):
        num_r = len(matrix) #数组的行数
        num_c = len(matrix[0])#数组的列数
        #对二维数组按列读取依次添加到列表1，然后列数个列表1再都添加到新的列表2，对这个新列表2倒转
        #列表2就是反转后的新二维数组
        newlist2 = []
        for i in range(num_c):
            newlist1 = []
            for j in range(num_r):
                newlist1.append(matrix[j][i])
            newlist2.append(newlist1)
        newlist2.reverse()
        return newlist2
'''
链接：https://www.nowcoder.com/questionTerminal/9b4c81a02cd34f76be2659fa0d54342a
来源：牛客网
思想，用左上和右下的坐标定位出一次要旋转打印的数据，一次旋转打印结束后，
往对角分别前进和后退一个单位.

 提交代码时，主要的问题出在没有控制好后两个for循环，需要加入条件判断，
防止出现单行或者单列的情况。'''
class Solution2:
    def printMatrix(self, matrix):
        row = len(matrix)
        column = len(matrix[0])
        result = []
        if row == 0 or column == 0:
            return []
        left = 0
        right =column-1
        top = 0
        bottom = row-1
        while left <= right and top <= bottom:
            l = left;r = right; t = top;b =bottom
            #从左到右
            while l <= right:
                result.append(matrix[top][l])
                l += 1
            #从上到下
            while t+1 <= bottom:
                result.append(matrix[t+1][right])
                t += 1
            #从右到左
            if top != bottom:
                while r-1 >= left:
                    result.append(matrix[bottom][r-1])
                    r -=1
            #从下到上
            if left != right:
                while b-1 > top:
                    result.append(matrix[b-1][left])
                    b -= 1
            left += 1;right -= 1;top += 1;bottom -= 1
        return result


matrix2 = [[1],[2],[3],[4],[5]]
matrix1 = [[1,2],[3,4]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
s = Solution2()
result = s.printMatrix(matrix2)
print(result)
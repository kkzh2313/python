'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, k, rows, cols):
        #首先建立布尔数组，检测格点是否之前已经记录过
        visited = [False]*(rows*cols)
        count = self.movingCountCore(k,rows,cols,0,0,visited)
        return count
    #2/记录合格的格点数目的函数
    def movingCountCore(self,k,rows,cols,row,col,visited):
        count = 0
        if self.check(k,rows,cols,row,col,visited):
            visited[row*cols+col] = True #记录当前格点状态为已走过
            count = 1+ self.movingCountCore(k,rows,cols,row,col-1,visited) + \
                       self.movingCountCore(k, rows, cols, row-1, col, visited) + \
                       self.movingCountCore(k, rows, cols, row, col+1, visited) + \
                       self.movingCountCore(k, rows, cols, row+1, col, visited)
        return count
    #统计该点是否满足条件
    def check(self,k,rows,cols,row,col,visited):
        if 0<=row<rows and 0<=col<cols and not visited[row*cols+col] and \
        self.getDigitSum(row)+self.getDigitSum(col)<=k:
            return True
    #行坐标和列坐标数位之和
    def getDigitSum(self,num):
        sum = 0
        while num:
            sum += num%10
            num = num//10
        return sum
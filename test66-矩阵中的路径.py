'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如 [[a b c e], [s f c s], [a d e e]] 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''
'''链接：https://www.nowcoder.com/questionTerminal/c61c6999eecb4b8f88a98f66b273a3cc
来源：牛客网

分析：回溯算法
 这是一个可以用回朔法解决的典型题。首先，在矩阵中任选一个格子作为路径的起点。如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的
第i个位置。如果路径上的第i个字符正好是ch，那么往相邻的格子寻找路径上的第i+1个字符。除在矩阵边界上的格子之外，其他格子都有4个相邻的格子。
重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。
　　由于回朔法的递归特性，路径可以被开成一个栈。当在矩阵中定位了路径中前n个字符的位置之后，在与第n个字符对应的格子的周围都没有找到第n+1个
字符，这个时候只要在路径上回到第n-1个字符，重新定位第n个字符。
　　由于路径不能重复进入矩阵的格子，还需要定义和字符矩阵大小一样的布尔值矩阵，用来标识路径是否已经进入每个格子。 当矩阵中坐标为（row,col）的
格子和路径字符串中相应的字符一样时，从4个相邻的格子(row,col-1),(row-1,col),(row,col+1)以及(row+1,col)中去定位路径字符串中下一个字符
如果4个相邻的格子都没有匹配字符串中下一个的字符，表明当前路径字符串中字符在矩阵中的定位不正确，我们需要回到前一个，然后重新定位。
　　一直重复这个过程，直到路径字符串上所有字符都在矩阵中找到合适的位置'''
# -*- coding:utf-8 -*-
'''
链接：https://www.nowcoder.com/questionTerminal/c61c6999eecb4b8f88a98f66b273a3cc
来源：牛客网

分析：回溯算法
 这是一个可以用回朔法解决的典型题。首先，在矩阵中任选一个格子作为路径的起点。如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的
第i个位置。如果路径上的第i个字符正好是ch，那么往相邻的格子寻找路径上的第i+1个字符。除在矩阵边界上的格子之外，其他格子都有4个相邻的格子。
重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。
　　由于回朔法的递归特性，路径可以被开成一个栈。当在矩阵中定位了路径中前n个字符的位置之后，在与第n个字符对应的格子的周围都没有找到第n+1个
字符，这个时候只要在路径上回到第n-1个字符，重新定位第n个字符。
　　由于路径不能重复进入矩阵的格子，还需要定义和字符矩阵大小一样的布尔值矩阵，用来标识路径是否已经进入每个格子。 当矩阵中坐标为（row,col）的
格子和路径字符串中相应的字符一样时，从4个相邻的格子(row,col-1),(row-1,col),(row,col+1)以及(row+1,col)中去定位路径字符串中下一个字符
如果4个相邻的格子都没有匹配字符串中下一个的字符，表明当前路径字符串中字符在矩阵中的定位不正确，我们需要回到前一个，然后重新定位。
　　一直重复这个过程，直到路径字符串上所有字符都在矩阵中找到合适的位置
'''


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return False
        visited = [0] * (rows * cols)

        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        if len(path) == pathLength:
            return True

        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == path[pathLength] and not \
        visited[row * cols + col]:

            pathLength += 1
            visited[row * cols + col] = True

            hasPath = self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, visited)

            if not hasPath:
                pathLength -= 1
                visited[row * cols + col] = False

        return hasPath

s = Solution()
ifTrue = s.hasPath("ABCESFCSADEE", 3, 4, "ABCCED")
ifTrue2 = s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM")
print(ifTrue2)

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows<=0 or cols<=0 or path==None:
            return False
        visited = [False]*(rows*cols) #建立一个布尔类型的数组，为False表示该格点未走过，True表示已走过
        pathLength = 0 # ----该变量是字符串的索引位置，起始从0开始，直到整个字符串路径都找到
        #下面开始遍历整个矩阵格点,一行行开始遍历
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix,rows,cols,row,col,path,pathLength,visited):
                    return True
        #整个遍历完都没找到，就表示不存在
        return False
    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        if pathLength == len(path):#如果索引到达整个字符串路径结束，说明里面有这么一个路径
            return True
        hasPath = False # 预先定义一个结果，默认矩阵中不存在一个这样的路径
        #下面开始寻找路径，即当前矩阵格点对应路径串的第pathlength位置的字符，且这个格点之前也未从遍历过
        if 0<=row<rows and 0<=col<cols and matrix[row*cols+col]==path[pathLength] and not visited[row*cols+col]:
            #对应的格点为True，表示已遍历该点
            visited[row*cols+col] = True
            pathLength += 1 #路径索引加1，
            # 开始检索后面的字符是否也在该矩阵格点四周，一直递归下去,看hasPath的状态
            hasPath = self.hasPathCore(matrix, rows, cols, row, col-1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row-1, col, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col+1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row+1, col, path, pathLength, visited)
            if hasPath == False: #r如果矩阵该格点的四周都没有找到合适的下一个字符
                pathLength -= 1
                visited[row*cols+col] = False
        return hasPath
                

                      '''注意：row与rows的关系，0<=row<rows，右边不能取等于'''
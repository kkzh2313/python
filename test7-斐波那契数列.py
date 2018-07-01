'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''
#不用递归
class Solution1:
    def Fibonacci(self,n):
        first,second = 0,1
        while n>0:
            second += first
            first = second - first
            n -= 1
        return first
class Solution2:
    def Fibonacci(self, n):
        # write code here
        if n < 0:
            return -1
        if 0<=n<2:
            return n
        first =0
        second=1
        while n>=2:
            current =first+second
            first = second
            second = current
            n-=1
        return current
if __name__ == '__main__':
    import time
    start1 = time.clock()
    s1 = Solution1()
    print(s1.Fibonacci(39))
    end1 = time.clock()
    print(end1-start1)

    start2 = time.clock()
    s2 = Solution2()
    print(s2.Fibonacci(39))
    end2 = time.clock()
    print(end2-start2)
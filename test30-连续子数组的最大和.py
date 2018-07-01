'''
题目描述
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''

'''
思路：
关键的问题在于成功分析整个过程。对于连续子数组，可以用一个数值来存储当前和，
如果当前和小于零，那么在进行到下一个元素的时候，直接把当前和赋值为下一个元素，
如果当前和大于零，则累加下一个元素，同时用一个maxNum存储最大值并随时更新。
也可以利用动态规划解决。
'''
#如果当前和小于0，就舍弃重新 取数组当前数作为当前累加和
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == None or len(array)<=0:
            return 0
        CurrentSum = 0 #表示当前加起来的和
        MaxSum = array[0]
        for i in array:
            if CurrentSum<=0:
                CurrentSum = i
            else:
                CurrentSum += i
            if CurrentSum > MaxSum:
                MaxSum = CurrentSum
        return MaxSum

    #方法二动态规划
    def FindGreatestSumOfSubArray2(self, array):
        if array == None or len(array)<=0:
            return 0
        Sum = [0]*len(array)
        for i in range(len(array)):
            if i == 0 or Sum[i-1]<=0:
                Sum[i] = array[i]
            # if i != 0 and Sum[i-1]>0:
            else:
                Sum[i] = Sum[i-1]+array[i]
        return max(Sum)

array = [1,-2,3,10,-4,7,2,-5]
s= Solution()
print(s.FindGreatestSumOfSubArray2(array))
list=[1,2]
list.sort()
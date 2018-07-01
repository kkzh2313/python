'''
题目描述
输入n个整数，找出其中最小的K个数。

例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,
'''

'''
思路二：不改变原数组
 # O(nlogk)的算法, 适合海量数据
# 利用一个k容量的容器存放数组, 构造最大堆, 
当下一个数据大于最大数, 跳过, 小于最大数, 则进入容器替换之前的最大数
'''
#Python入门之堆（heapq）https://zhuanlan.zhihu.com/p/28246243
# -*- coding:utf-8 -*-
class Solution:

    def GetLeastNumbers_Solution(self,tinput,k):
        import heapq
        #首次进行特殊情况的判断
        if tinput==None or len(tinput)<=0 or len(tinput)<k or k<=0:
            return []
        output = []
        for i in tinput:
            #遍历输入数组，建立一个k长度数组用来存取最小的k个数。若长度不为k，就将数加到output数组里
            #达到长度k(即存满了)，就对数组进行最大堆构造。接下来比较传入的数字与最大堆顶点的大小，若比顶点大就继续下一个数字遍历，若小，就替换掉该顶点
            if len(output)<k:#
                output.append(i)
            else:
                output = heapq.nlargest(k,output)
                if i >= output[0]:
                    continue
                else:
                    output[0] = i
        return sorted(output) ###参考给的是output[::-1]，在k=n的时候不是排好序的

'''
解法一 是基于划分的方法，如果是查找第k个数字，
第一次划分之后，划分的位置如果大于k，那么就在前面的子数组中进行继续划分，
反之则在后面的子数组继续划分，时间复杂度O(n)；
'''
class Solution2:

    def GetLeastNumbers_Solution(self,tinput,k):
        if tinput == None or len(tinput)<=0 or len(tinput)<k or k<=0:
            return None
        n = len(tinput)
        start = 0
        end = n-1
        index = self.partition(tinput,start,end)
        while index != k-1:
            if index < k-1:
                start = index+1
                index = self.partition(tinput,start,end)
            else:
                end = index -1
                index = self.partition(tinput,start,end)
        output = tinput[:k]
        return sorted(output)

    #快速排序的切分函数表示
    def partition(self,numbers,low,high):
        if numbers == None or len(numbers)<=0 or low<0 or high>=len(numbers):
            return None
        pivotkey = numbers[low] #选择第一个数作为枢纽值        --------这里要注意
        while low < high:
            # 如果high指针指的数比枢纽大，high指针一直往前走
            #（找到一个位置放下枢纽值使其后面的数都比它大）
            while low<high and numbers[high]>=pivotkey:
                high -= 1
            numbers[low],numbers[high] = numbers[high],numbers[low]
            #如果low指针指的数比枢纽值大，low指针一直往后走
            while low < high and numbers[low]<=pivotkey:
                low += 1
            numbers[low],numbers[high]= numbers[high],numbers[low]
        return low #直到low与high所指位置一样，就是枢纽正确放置的位置，



tinput = [4,5,1,6,2,7,3,8]
s = Solution2()
# output = s.GetLeastNumbers_Solution(tinput, 8)
print(s.GetLeastNumbers_Solution(tinput, 6))
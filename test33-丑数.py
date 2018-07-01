#此题注意各变量是从0开始还是从1开始，循环的条件是什么

'''
题目描述
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

'''
空间换时间。建立一个长度为n的数组，保存这n个丑数。
在进行运算的时候，某个位置需要求得丑数一定是前面某个丑数乘以2、3或者5的结果，
假设数组已有排好序的丑数，最大丑数记为M。
我们分别记录M之前乘以2后能得到的大于M的丑数中最小的记为M2，乘以3后大于M中最小的记为M3，乘以5后大于M中最小的记为M5，
那么下一个丑数一定是M2，M3，M5中的最小的那一个。
同时注意到，已有的丑数是按顺序存放在数组中的。对乘以2而言，肯定存在某一个丑数T2，
排在他之前的每一个丑数乘以2得到的结果都会小于已有的最大丑数，在他之后的每一个丑数乘以2得到的结果都会太大，
我们只需记下这个丑数的位置，每次生成新的丑数的时候，去更新这个T2。对于3和5同理。'''

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        uglyNumber = [1]*index #定义一个index长度的数组，用来存放丑数
        nextIndex = 1 #丑数数组固定第一个就是1，开始更新从第二个开始
        index2 = 0 #下面三条用来定义丑数2、3/5 倍数的坐标
        index3 = 0
        index5 = 0
        while nextIndex<index:
            #丑数就是这几个数中最小的
            minval = min(uglyNumber[index2]*2,uglyNumber[index3]*3,uglyNumber[index5]*5)
            uglyNumber[nextIndex] = minval
            #更新丑数2/3/5倍对应坐标
            while uglyNumber[index2]*2<=uglyNumber[nextIndex]:
                index2 += 1
            while uglyNumber[index3]*3 <= uglyNumber[nextIndex]:
                index3 += 1
            while uglyNumber[index5]*5<=uglyNumber[nextIndex]:
                index5 += 1

            nextIndex += 1
        return uglyNumber[-1]
'''
普通方法一个数挨个确定是否为丑数'''
class Solution2:
    def GetUglyNumber_Solution(self, index):
        if index<=0:
            return 0
        number = 0 #数字从0开始往后遍历来确定是否为丑数
        uglyFound = 0 #0除外第几个丑数
        while uglyFound<index:
            number += 1
            if self.IsUgly(number):
                uglyFound += 1

        return number
    def IsUgly(self,number):
        while number%2==0:
            number = number/2
        while number%3==0:
            number = number/3
        while number%5 ==0:
            number = number/5
        return True if number==1 else False





s=Solution2()
print(s.GetUglyNumber_Solution(8))

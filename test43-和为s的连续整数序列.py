'''
找出所有和为S的连续正数序列
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''

'''
设定两个指针，先分别指向数字1和数字2，并设这两个指针为small和big，
对small和big序列之间的数求和，如果和大于目标值，则从当前和中删除small值，并把small值加一，
如果和小于目标值，则把big值加一，再把新的big值加入和中。
如果和等于目标值，就输出small到big的序列，同时把big加一并加入和中，继续之前的操作。

因为序列至少要有两个数字，我们一直增加small到中间位置（1+s）//2为止
'''
# -*- coding:utf-8 -*-
##上面剑指offer思路
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3: #至少两个数，最小为1,2序列其和最小为3
            return []
        small , big = 1,2
        middle = (1+tsum)>>1
        cursum = small + big
        result = []
        while small < middle :
            if cursum == tsum:
                result.append(list(range(small,big+1)))
                big += 1
                cursum += big
            elif cursum < tsum:
                big += 1
                cursum += big
            else:
                cursum -= small
                small += 1
        return result


##s双指针技术，相当于一个窗口，窗口左右两边就是两个指针。
# 根据窗口内值的和来确定窗口位置和宽度。
#结束条件是窗口宽度变为1，即low high指针重合，--大概也是在跑到中间附近时候

class Solution2:
    def FindContinuousSequence(self, tsum):
        if tsum <3:
            return []
        #两个起点，相当于动态窗口的两边，根据其窗口内的值的和来确定窗口的位置和大小
        low, high = 1,2
        result = []
        while low < high:
            #由于是连续的，差为1的一个序列，那么求和公式是(a0+an)*n/2
            cursum = ((low+high)*(high-low+1))>>1
            #相等，那么就将窗口范围的所有数添加进结果集，窗口长度不变 整体右滑前进
            if cursum == tsum:
                result.append(list(range(low,high+1)))
                low += 1
            #如果当前窗口内的值之和大于sum，那么左边窗口右移一下
            elif cursum > tsum:
                low += 1
            #如果当前窗口内的值之和小于sum，那么右边窗口右移一下
            else:
                high += 1
        return result


s = Solution2()
print(s.FindContinuousSequence(4))
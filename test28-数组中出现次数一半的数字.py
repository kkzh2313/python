'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

'''
解法二根据数组特点找出o(n)算法
保存两个数一个是数组中的一个数组数字。如果下一个数字和当前保存的数字相同，次数加1
不同   次数减1   。。
要找的数字的肯定是最后一次把次数设为1时对应的数字
'''


# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if numbers == None:
            return 0
        length = len(numbers)
        result = numbers[0]
        times = 1
        for i in range(1, length):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        if not self.CheckMoreThanHalf(numbers, length, result):
            return 0
        return result


    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):  # 遍历全部数组，看所找的数字结果
            if numbers[i] == number:
                times += 1
        if times * 2 <= length:
            return False
        return True
S = Solution()
print(S.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))




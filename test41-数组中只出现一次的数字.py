
'''
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
'''
'''
任何一个数字异或他自己都等于0，0异或任何一个数都等于那个数。
数组中出了两个数字之外，其他数字都出现两次，那么我们从头到尾依次异或数组中的每个数，
那么出现两次的数字都在整个过程中被抵消掉，那两个不同的数字异或的值不为0，也就是说这两个数的异或值中至少某一位为1。
我们找到结果数字中最右边为1的那一位i，然后一次遍历数组中的数字，
如果数字的第i位为1，则数字分到第一组，数字的第i位不为1，则数字分到第二组。这样任何两个相同的数字就分到了一组，而两个不同的数字在第i位必然一个为1一个不为1而分到不同的组，
然后再对两个组依次进行异或操作，
最后每一组得到的结果对应的就是两个只出现一次的数字。
'''

class Solution:
    def FindNumsAppearOnce(self, array):
        if array == None or len(array)<=0:
            return []
        #第一轮循环找出两个出现一次数异或的结果，就是对所有数进行异或
        tmp = 0
        for i in array:
            tmp = tmp^i
        #获取异或结果tmp最低位1的所在位
        index = 0 #数字二进制最右边为最低位，设为0
        while tmp & 1 == 0:
            tmp = tmp>>1
            index += 1
        #第二轮循环列表，对index位为1的数进行异或,找出一个出现一次的数
        #对index位为0的所有数进行异或可以找出另一个出现一次的数
        num1 = num2 = 0
        for i in array:
            if self.IsBit(i,index):
                num1 ^= i
            else:
                num2 ^= i
        return [num1,num2]

    def IsBit(self,number,index):#传入列表的各个数值，两个不同数最右不同 所在的位数
        number =number>>index
        return number&1

s=Solution()
list1=[1,1,2,2,3,4,4,5]
list2 = [1,2]
print(s.FindNumsAppearOnce(list2))

'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
'''

'''
#剑指offer的方法3， 比较难想到且交换比较容易搞错 ----时间复杂度为（n）,在原数组上调换位置所以空间复杂度为（1） 
# 从头到尾依次扫描这个数组中的每个数字，
如果下标i不是出现数字i，那么就把数字i和i处的数字进行交换使数字i出现在应该出现的位置，
如果新交换的数字还不是他应该出现的位置，继续交换，直至该处的数字m等于x下标m，如果在交换的过程中，
第i处的位置数字等于第m处的数字，那么我们就找到了第一个重复的数字，记录这个数字，在从下一个位置继续扫描。

'''
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if numbers == None or len(numbers)<1:
            return False
        length = len(numbers)
        #遍历数组，如果里面的数字不在0-（n-1）之间 就报错
        for i in range(length):
            if numbers[i]<0 or numbers[i]>length-1:
                return False
        #开始扫描数组 进将数字交换到正确的位置
        for i in range(length):

            # index = numbers[i] #这一句不能提前出现这里 #将i位置对应的数字定义为索引，与该索引所对应位置的数进行比较
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0]= numbers[i]
                    print(duplication[0])
                    return True
                else:
                    index= numbers[i]
                    numbers[i],numbers[index] = numbers[index],numbers[i]
                    # numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i] #不能这么写，会造成混乱。
        return False


''''另外的方法是建立一个新的数组，对应索引位置放该数的个数
或者建立一个字典类似哈希表
#时间复杂度是（n）,空间复杂度也是（n）
'''
class Solution2:
    def duplicate(self, numbers, duplication):
        if numbers == None or len(numbers)<1:
            return False
        length = len(numbers)
        #先遍历数组，检查里面的数字在不在0-(length-1)之间 就报错
        for i in numbers:
            if i<0 or i>length-1:
                return False
        alist = [0]*length
        #再次遍历数组，对辅助数组的元素进行相应的变动
        for i in numbers:
            if alist[i] >= 1: #如果辅助数组该位置存的数不是0，表示之前原数组已经存在该数
                duplication[0] = i
                print(duplication[0])
                alist[i] += 1
                return True
            else:
                alist[i] += 1
        return False





test = [4, 3, 1, 2, 2, 5, 3]
s = Solution2()
dupulication = [0]
print(s.duplicate(test,dupulication))
# print(s.duplicate(test))



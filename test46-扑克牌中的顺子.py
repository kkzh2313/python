'''
随机从扑克牌中抽出了5张牌,判断是不是顺子,
决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
'''

'''
剑指思路：1排序   2. 统计数组中0的个数     3. 统计排序数组中相邻数字之间的空缺总数
如果2》=3那么就是顺子     如果有顺子那么就肯定不是顺子
'''
class Solution:
    def IsContinuous(self,numbers):
        if numbers == None or len(numbers)!=5:
            return False
        numbers = sorted(numbers)
        numberZero = 0
        numberInterval = 0
        #开始循环遍历数组的数，统计2.3两种情况下的个数
        i = 0
        while i < len(numbers)-1:
            if numbers[i] == 0:
                numberZero += 1
                i += 1  #别漏了这句
                continue
            if numbers[i] == numbers[i+1]:
                return False
            numberInterval += numbers[i+1]-numbers[i]-1
            i += 1
        #判断两种情况数目的大小
        if numberZero >= numberInterval:
            return True
        return False


#另外有个思路是：观察数组可知 是顺子  必须满足两个条件：（除零外） 1 最大，最小值之差<5    2.不能有重复的数

s=Solution()
test = [1,0,3,5,4]
print(s.IsContinuous(test))

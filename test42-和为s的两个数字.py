'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''

'''时间复杂度为n
设定两个指针，一个指向数组的起点，一个指向数组的终点，然后对两个数字求和，
1、如果和大于目标值，则把后一个指针前移 2、如果和小于目标值，则把前一个指针后移。
两个指针交汇的时候如果还没找到，就终止操作。

---------至于乘积最小的两个数，因为和一定的时候 两个数的间隔越大 乘积越小。（类比长方形）
'''
class Solution:
    def FindNumbersWithSum(self, array, tsum):#传入排序数组   数字和
        if array == None or len(array)<=0 or array[-1]+array[-2]<tsum:
            return []
        start = 0 #定义第一个指针
        end = len(array)-1 #定义第二个指针
        while start < end :
            sum = array[start]+array[end]
            if sum > tsum:
                end -= 1
            elif sum<tsum:
                start += 1
            else:
                return [array[start],array[end]]
        return []  #如果上面的循环结束都没找到就说明没有这么两个数
test = [1,2,4,7,11,15]
number = 15
s = Solution()
print(s.FindNumbersWithSum(test,number))



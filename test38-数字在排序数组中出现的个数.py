'''
统计一个数字在排序数组中出现的次数。
'''
#是使用二分查找的方法依次找到最开始的k和最后出现的k,两者位置相减就是k总共出现的次数

class Solution:
    def GetNumberOfK(self,data,k):
        length = len(data)
        #特殊情况：为输入空指针，空数组，或者所找的k不在数组里出现
        if data == None or length <= 0 or k not in data:
            return 0

        first = self.GetFirstK(data,k,0,length-1)
        last = self.GetLastK(data,k, 0,length-1)
        if first != -1: #注意这里加判断
            number = last - first +1
        return number

    def GetFirstK(self,data, k, start, end):
        if start > end : ##########判断异常
            return -1

        middleIndex = (start+end)//2 #二分查找  中间位置
        middleData = data[middleIndex] #中间对应的数字， 下面要用其跟所找数字进行比较
        if middleData == k:
            if (middleIndex >0 and data[middleIndex-1]!=k) or middleIndex == 0: #'''注意两种情况'''是递归最后结束的情况
                return middleIndex
            else:
                end = middleIndex - 1
        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1
        return self.GetFirstK(data,k,start,end)

    def GetLastK(self,data, k , start, end):
        if start > end : ##########判断异常
            return -1
        length = len(data)
        middleIndex = (start+end)//2 #二分查找  中间位置
        middleData = data[middleIndex] #中间对应的数字， 下面要用其跟所找数字进行比较
        if middleData == k:
            if (middleIndex < length-1 and data[middleIndex+1]!=k) or middleIndex == length-1: #'''注意两种情况'''是递归最后结束的情况
                return middleIndex
            else:
                start = middleIndex + 1
        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1
        return self.GetLastK(data,k,start,end)

alist = []
s = Solution()
print(s.GetNumberOfK(alist, 6))
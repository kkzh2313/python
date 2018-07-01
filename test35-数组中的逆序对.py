'''
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
'''
'''
归并排序的思路：【7,5,6,4】为例
链接：https://www.nowcoder.com/questionTerminal/96bd6684e04a44eb80e6a68efc0ec6c5
来源：牛客网

(a) 把长度为4的数组分解成两个长度为2的子数组；
(b) 把长度为2的数组分解成两个成都为1的子数组；
(c) 把长度为1的子数组 合并、排序并统计逆序对 ；
(d) 把长度为2的子数组合并、排序，并统计逆序对；
链接：https://www.nowcoder.com/questionTerminal/96bd6684e04a44eb80e6a68efc0ec6c5
来源：牛客网

在上图（a）和（b）中，我们先把数组分解成两个长度为2的子数组，
再把这两个子数组分别拆成两个长度为1的子数组。
接下来一边合并相邻的子数组，一边统计逆序对的数目。在第一对长度为1的子数组{7}、{5}中7大于5，因此（7,5）组成一个逆序对。
同样在第二对长度为1的子数组{6}、{4}中也有逆序对（6,4）。由于我们已经统计了这两对子数组内部的逆序对，
因此需要把这两对子数组 排序 如上图（c）所示， 以免在以后的统计过程中再重复统计。


#################
过程：先把数组分割成子数组，先统计出子数组内部的逆序对的数目，
然后再统计出两个相邻子数组之间的逆序对的数目。在统计逆序对的过程中，还需要对数组进行排序。
如果对排序算法很熟悉，我们不难发现这个过程实际上就是归并排序
'''

import copy as cp
class Solution:
    def InversePairs(self, data):
        length = len(data)
        if data == None or length <= 0:
            return 0
        # copy = [0]*length
        # for i in range(length):
        #     copy[i] = data[i]
        #直接用copy = data 就会出错，后面copy变data也跟着变
        # copy = cp.copy(data)#方法2引入copy模块
        copy = data.copy()
        count = self.InversePairsCore(data, copy, 0, length-1)
        return count
    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start)//2 #分割
        left = self.InversePairsCore( copy,data, start, start+length)
        right = self.InversePairsCore( copy,data, start+length+1, end)
        # left = self.InversePairsCore( data, copy,start, start+length) ##这里如果先定义data结果不对,多加1了
        # right = self.InversePairsCore( data, copy, start+length+1, end)

        # i初始化为前半段最后一个数字的下标
        i = start + length
        # j初始化为后半段最后一个数字的下标
        j = end
        #书上的p3指针下标，初始为最后。即排序新数组从后往前排序
        indexCopy = end
        count = 0
        while i >= start and j >= start+length+1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start+length+1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count
s = Solution()
# print (s.InversePairs([7,5,6,4]))
print(s.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]))

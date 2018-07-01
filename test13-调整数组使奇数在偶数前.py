'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
##python偷懒技巧 ，
# #依次遍历，发现是奇数就放在一个数组里，是偶数就放在另一个数组
class Solution1:
    def reOrderArray(self, array):
        # write code here
        if len(array) < 1:
            return []
        if len(array) == 1:
            return array

        left = [i for i in array if i & 0x1]
        right = [i for i in array if not i & 0x1]
        return left + right

######类似冒泡排序
class Solution2:
    def reOrderArray(self, array):
        l= len(array)
        i = 0
        while i < l:
            j = l - 1
            while j>i:
                if array[j]%2==1 and array[j-1]%2==0:#前面的是偶数就换位置
                    array[j-1],array[j]=array[j],array[j-1]

                j-=1

            i+=1
        return array
s = Solution2()
print(s.reOrderArray([1,2,3,4,5,6,7]))
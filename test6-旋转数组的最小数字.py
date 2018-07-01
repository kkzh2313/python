'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

'''
链接：https://www.nowcoder.com/questionTerminal/9f3231a991af4f55b95579b44b7a01ba
来源：牛客网

采用二分法解答这个问题，
mid = low + (high - low)/2
需要考虑三种情况：
(1)array[mid] > array[high]:
出现这种情况的array类似[3,4,5,6,0,1,2]，此时最小数字一定在mid的右边。
low = mid + 1
(2)array[mid] == array[high]:
出现这种情况的array类似 [1,0,1,1,1] 或者[1,1,1,0,1]，此时最小数字不好判断在mid左边
还是右边,这时只好一个一个试 ，
high = high - 1
(3)array[mid] < array[high]:
出现这种情况的array类似[2,2,3,4,5,6,6],此时最小数字一定就是array[mid]或者在mid的左
边。因为右边必然都是递增的。
high = mid
注意这里有个坑：如果待查询的范围最后只剩两个数，那么mid 一定会指向下标靠前的数字
比如 array = [4,6]
array[low] = 4 ;array[mid] = 4 ; array[high] = 6 ;
如果high = mid - 1，就会产生错误， 因此high = mid
但情形(1)中low = mid + 1就不会错误
'''
'''补充：剑指offer里有一种情况：前面的0个元素搬到后面即排序数组本身，只需返回第一个元素就是待求的最小元素'''

class Solution1:
    def minNumberInRotateArray(self,rotateArray):
#定义两个变量（代表指针），low指向搜查数组的头元素，high指向最后元素
  #结束条件是low不小于high结束，并返回low位置的数就是所要找的最小数
        if len(rotateArray) == 0:
            return 0
        low = 0
        high = len(rotateArray)-1
        if rotateArray[low]<rotateArray[high]:#buchong部分，
            return rotateArray[low]
        while low < high:
            mid = low + (high-low)//2
            if rotateArray[mid] > rotateArray[high]:
                low =mid+1
            elif rotateArray[mid]==rotateArray[high]:
                high = high-1
            else:
                high = mid
        return rotateArray[low]

#######比第三种方法稍微好点，不用遍历全部数组,但是也是O（n）的复杂度
class Solution2:
    def minNumberInRotateArray(self,rotateArray):
        if len(rotateArray)==0:
            return 0
        for i in range(0,len(rotateArray)):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]
        return rotateArray[0]

####普通方法，遍历数组，复杂度在0（n）
class Solution3:
    def minNumberInRotateArray(self,rotateArray):
        if len(rotateArray)==0:
            return 0
        min = rotateArray[0]
        for i in rotateArray:
            if i < min :
                min = i
        return min
if __name__ == '__main__':
    s = Solution1()
    alist1 = []
    alist2 = [1,0,1,1,1]
    alist3 = [3,4,5,1,2]
    alist4 = [2,2,3,4,5]
    # print(s.minNumberInRotateArray(alist1))
    print(s.minNumberInRotateArray(alist2))
    # print(s.minNumberInRotateArray(alist3))
    print(s.minNumberInRotateArray(alist4))


'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''
######----时间效率考虑选择用最大堆 最小堆来解决
'''思路一
排序的数组来看中位数为界被分成两部分左边都是小于中位数右边大，构建两个堆，左边为最大堆 右边为最小堆

1、当目前两堆总数为偶数的时候，把新来的数字存入最大堆，然后重排最大堆（这里和下面注意合为一起，两个堆都排），
        如果最大堆的堆顶数字大于最小堆堆顶数字，则把两个堆顶数字交换，
    重排两堆，此时两堆数字总数为奇数，直接输出最大堆堆顶数字即为中位数；
2、如果当前两堆总数为奇数的时候，把新来的数字存入最小堆，重排最小堆，
        如果最大堆的堆顶数字大于最小堆堆顶数字，则把两个堆顶数字交换，
    重排两堆，此时两堆数字总数为偶数，取两堆堆顶数字做平均即为中位数。
'''

'''剑指offer思路：
插入：
  是当前是偶数时将新数插入到最小堆，插入之前为了避免该数比最大堆里的数要小，先放到最大堆里然后将堆顶的数传入最小堆
  若当前的数据总数个数是奇数，将新数放到最大堆；插入之前先放进最小堆，然后弹出最小堆的堆顶的数，放进最大堆里
求中位数：
  数据流总个数是偶数--就返回两个堆的堆顶数平均值
** 数据流总个数是奇数--就返回最小堆的堆顶数！！！！

'''
# -*- coding:utf-8 -*-
import heapq
class Solution:
    def __init__(self):
        self.headMax = []
        self.headMin = []
        self.count = 0  #记录数据总个数
    def Insert(self,num):
        # # 个数是偶数，就要放到最小堆里，但之前先放进最大堆将堆顶放进最小堆
        # if self.count &1 ==0:
        #     newnum = heapq.heappushpop(self.headMax,-num) #将新数加入最大堆然后弹出新的堆顶（最大数）,注意heapq模块默认是最小堆，所以最大堆用相反数传入传出来实现
        #
        #     heapq.heappush(self.headMin,-newnum)
        # else:
        #     newnum = heapq.heappushpop(self.headMin,num)
        #     heapq.heappush(self.headMax,-newnum)
        # self.count += 1

        # 个数是偶数，就要放到最小堆里，但之前先放进最大堆将堆顶放进最小堆
        if self.count &1 ==0:
            heapq.heappush(self.headMax,-num)
            newnum1 = heapq.heappop(self.headMax)
            heapq.heappush(self.headMin,-newnum1)
        else:
            heapq.heappush(self.headMin,num)
            newnum2 = heapq.heappop(self.headMin)
            heapq.heappush(self.headMax,-newnum2)
        self.count += 1
    def GetMedian(self):
        # if self.count == 1:
        #     return num
        # numMaxhead = -(self.headMax[0])  #不要这么写会在输入第一个数的时候报错，因为
        if self.count &1 ==0:
            return (-(self.headMax[0])+self.headMin[0])/2.0
        else:
            return self.headMin[0]
s =Solution()
result = []
cishu = 0

while cishu <9:
    num = input()
    s.Insert(int(num))
    result.append(s.GetMedian())
    cishu += 1
print(result)


'''
测试用例:
[5,2,3,4,1,6,7,0,8]

对应输出应该为:

"5.00 3.50 3.00 3.50 3.00 3.50 4.00 3.50 4.00 "

你的输出为:

list index out of range
'''
'''
链接：https://www.nowcoder.com/questionTerminal/9be0172896bd43948f8a32fb954e1be1
来源：牛客网

private int count = 0;
private PriorityQueue<Integer> minHeap = new PriorityQueue<>();
private PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(15, new Comparator<Integer>() {
    @Override
    public int compare(Integer o1, Integer o2) {
        return o2 - o1;
    }
});
 
public void Insert(Integer num) {
    if (count %2 == 0) {//当数据总数为偶数时，新加入的元素，应当进入小根堆
        //（注意不是直接进入小根堆，而是经大根堆筛选后取大根堆中最大元素进入小根堆）
        //1.新加入的元素先入到大根堆，由大根堆筛选出堆中最大的元素
        maxHeap.offer(num);
        int filteredMaxNum = maxHeap.poll();
        //2.筛选后的【大根堆中的最大元素】进入小根堆
        minHeap.offer(filteredMaxNum);
    } else {//当数据总数为奇数时，新加入的元素，应当进入大根堆
        //（注意不是直接进入大根堆，而是经小根堆筛选后取小根堆中最大元素进入大根堆）
        //1.新加入的元素先入到小根堆，由小根堆筛选出堆中最小的元素
        minHeap.offer(num);
        int filteredMinNum = minHeap.poll();
        //2.筛选后的【小根堆中的最小元素】进入大根堆
        maxHeap.offer(filteredMinNum);
    }
    count++;
}
 
public Double GetMedian() {
    if (count %2 == 0) {
        return new Double((minHeap.peek() + maxHeap.peek())) / 2;
    } else {
        return new Double(minHeap.peek());
    }
}
'''
'''
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''
'''
 * 思路：滑动窗口应当是队列，但为了得到滑动窗口的最大值，队列序可以从两端删除元素，因此使用双端队列。(注意队列里保存的是原数组元素对应的索引下标)
 *     原则：
 *     对新来的元素k，将其与双端队列中的元素相比较
 *     1）前面比k小的，直接移出队列（因为不再可能成为后面滑动窗口的最大值了!）,
 *     2）前面比k大的X，比较两者下标，判断X是否已不在窗口之内，不在了，直接移出队列
 *     队列的第一个元素是滑动窗口中的最大值
'''
#该方法循环比较多
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        if not num or size <= 0:
            return []
        deque = []
        if len(num) >= size:
            index = []
            for i in range(size):
                while len(index) > 0 and num[i] > num[index[-1]]:
                    index.pop()
                index.append(i)

            for i in range(size, len(num)):
                deque.append(num[index[0]])
                while len(index) > 0 and num[i] >= num[index[-1]]:
                    index.pop()
                if len(index) > 0 and index[0] <= i - size:
                    index.pop(0)
                index.append(i)

            deque.append(num[index[0]])
        return deque
if __name__ == '__main__':
    test = [2, 3, 4, 2, 6, 2, 5, 1]
    s = Solution()
    print(s.maxInWindows(test, 3))

'''
链接：https://www.nowcoder.com/questionTerminal/1624bc35a45c42c0bc17d17fa0cba788
来源：牛客网

//引用马客（Mark）的解题思路，马客没加注释，我用自己的理解加下注释，希望对你们有用，
//如有错误，见谅，我会及时修改。
//deque s中存储的是num的下标
class Solution {
public:
    vector<int> maxInWindows(const vector<int>& num, unsigned int size)
    {
        vector<int> res;
        deque<int> s;
        for(unsigned int i=0;i<num.size();++i){
            while(s.size() && num[s.back()]<=num[i])//从后面依次弹出队列中比当前num值小的元素，同时也能保证队列首元素为当前窗口最大值下标
                s.pop_back();
            while(s.size() && i-s.front()+1>size)//当当前窗口移出队首元素所在的位置，即队首元素坐标对应的num不在窗口中，需要弹出
                s.pop_front();
            s.push_back(i);//把每次滑动的num下标加入队列
            if(size&&i+1>=size)//当滑动窗口首地址i大于等于size时才开始写入窗口最大值
                res.push_back(num[s.front()]);
        }
        return res;
    }
};

'''
class Solution1:
    def maxInWindows(self, num, size):
        if not num or size <= 0:
            return []
        res = []
        s =[]  #双端队列 存放索引
        for i in range(len(num)):
            while len(s) and num[s[-1]] <= num[i]:
                s.pop()
            while len(s) and i-s[0]+1 > size:
                s.pop(0)
            s.append(i)
            if i+1 >= size:
                res.append(num[s[0]])
        return res
s=Solution1()
num = [2, 3, 4, 2, 6, 2, 5, 1]
print(s.maxInWindows(num,3))

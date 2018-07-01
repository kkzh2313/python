'''
timu:一只青蛙一次可以跳上1级台阶，
也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。

'''
'''
思路：还是递归，斐波那契数列思路
跳一个台阶：一种跳法
2个台阶：1 1,2  共两种跳法
3个台阶：111，12,21 共三种跳法
4个台阶：1111,112,121,211,22 共四种跳法
n级台阶共有n-2级台阶跳法数+ n-1级台阶跳法 ，但 n=1,2时跳法是其本身n

'''
class solution:
    def jumpfloor(self,number):
        if number <=0:
            return 0
        if number==1 or number==2:
            return number

        first = 1
        second =2
        while number >= 3:
            current = first + second
            first =second
            second = current
            number-=1
        return current
#递归算法，超时
class solution1:
    def jumpfloor(self,number):
        if number <=0:
            return 0
        if number==1 or number==2:
            return number
        else:
            return self.jumpfloor(number-1)+self.jumpfloor(number-2)


# test = solution1()
# test_num = test.jumpfloor(3)
#
# print(test_num)


'''
一只青蛙一次可以跳上1级台阶，
也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
'''
思路：每个台阶都有跳与不跳两种情况（除了最后⼀个台阶），最后⼀个台阶必须跳。所以共⽤
2^(n-1)中情况。
'''
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return pow(2,number-1)

#矩形覆盖
class solution:
    def rectcover(self,number):
        if number <=0:
            return 0
        first,second = 1,2
        while number>1:
            second += first
            first = second - first
            number -= 1
        return first
if __name__ == '__main__':
    s = solution()
    print(s.rectcover(1))

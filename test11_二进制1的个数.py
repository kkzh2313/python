'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
'''

'''
思路一：按位确定是否位1，从最右位开始，&1，为1表示最右位是1，依次右移。
        注意：负数右移会在左边补1，为避免陷入无限循环，所以需要提前确定好右移次数为32次或二进制位为32位

思路二：常规做法，避免上述无限循环，&1操作后，1进行左移,直到右移32次 
    
思路三：
    注意到每个非零整数n和n-1进行按位与运算，整数n的二进制数中最右边的1就会变成0，
    那么二进制数中的1的个数就会减少一个，因此可以利用一个循环，使得 n = n&(n-1) ，
    计算经过几次运算减少到0，就是有几个1。（有几个1就几次循环）



扩展：判断一个数值是不是2得整数次方，如果是的话，这个数的二进制数中有且只有一个1，
那么这个数n会有 n&(n-1) == 0。
或者求两个整数m和n需要改变m二进制中的多少位才能得到n，
可以先做 m^n 的异或运算，然后求这个数中有多少个1。'''


# -*- coding:utf-8 -*-
class Solution1:
    def NumberOf1(self, n):
        # write code here
        # return sum([(n>>i & 1) for i in range(0,32)])
        count = 0
        for i in range(32):#因为整数int类型是32位，Python没有类型限制需要手动加上
            if (n>>i)&1:
                count += 1
        return count

#https://blog.csdn.net/u010005281/article/details/79851154  0&0xfffffff
class Solution2:
    def NumberOf1(self, n):
        # write code here
        count = 0
        # if n<0:
        n=n&0xFFFFFFFF #把负号去掉，如果负号在后面会陷入死循环
            #不是这个吧？应该是限制位数为32位，int型是32位长
        while n:
            n &= n-1
            count += 1
        return count

# -*- coding:utf-8 -*-
class Solution3:
    def NumberOf1(self, n):
        # write code here
        count=0
        nbin=bin(n&0xffffffff)
        return nbin.count('1')
if __name__ == '__main__':

    s=Solution2()
    print(s.NumberOf1(-1))
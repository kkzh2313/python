
'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''


'''将两个数的加法看作两步，
第一步是两个数相加但是不进位，第二步是记录之前的两数相加应该进位的地方加上前一个相加但是不进位的数。
对于具体的两个不小于0的数m和n，
第一步可以看做m和n的异或运算m^n，
第二步可以看做m和n的与运算然后左移一位得到实际的进位位置(m&n)<<1。
然后把两个得到的数字加起来继续操作，指到carry进位为0终止操作。对于含有负数的情况，
见博文https://blog.csdn.net/u012505432/article/details/51902155。

'''
class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            sum = num1 ^ num2
            carry = (num1 & num2)<<1
            num1 = sum & 0xffffffff
            num2 = carry

        #判断符号位是否为1做处理
        # if num1 >> 31 ==0:
        #     return num1
        # else:
        #     return num1-4294967296  #2**32(2的32次方)
        return num1 if num>>31==0 else num1-4294967296
s = Solution()
print(s.Add(4, -6))
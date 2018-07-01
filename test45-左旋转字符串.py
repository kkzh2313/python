'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
'''

#这一方法比书上更全面，不仅可以移动比字符串长度大的位数了
#“先补后切”  这里空间复杂度为O(N)，
class Solution:
    def LeftRotateString(self, s, n):
        # if len(s)<=0 or s==None or len(s)<n or n<0:
        if len(s) <= 0 or s == None  or n < 0:
            return ''
        length = len(s)

        n = n % length   ######很关键，因为n可能大于字符串的长度，所以得取余。就可以实现n>length 的字符翻转
        s += s
        return s[n:n+length]


#剑指offer的思路还是两次旋转  空间优化为O(1)了，时间为o（n）

class Solution2:
    # 一种方法是 先划分两部分，对每一部分进行翻转，然后对这一新的字符串进行整体翻转
    # def LeftRotateString(self, s, n):
    #     if s == None or len(s)<1 :
    #         return ''
    #     strlist = list(s)
    #     n = n % len(s)
    #     frontlist = self.Reverse(strlist[:n])
    #     behindlist = self.Reverse(strlist[n:])
    #     frontlist.extend(behindlist)
    #     resultlist = self.Reverse(frontlist)
    #     resultlist = ''.join(frontlist)
    #     return resultlist

    # 第二种方法 先整体翻转，再对划分的两部分依次翻转
    def LeftRotateString(self, s, n):
        if s == None or len(s)<1 :
            return ''
        length = len(s)
        strlist = list(s)
        strlist = self.Reverse(strlist)
        n = n % len(s)

        frontlist = self.Reverse(strlist[:length-n])
        behindlist = self.Reverse(strlist[length-n:])

        resultlist = ''.join(frontlist) + ''.join(behindlist)
        return resultlist

    def Reverse(self,alist):
        if alist == None or len(alist)<1:
            return ''
        start = 0
        end = len(alist)-1
        while start < end :
            alist[start],alist[end] = alist[end],alist[start]
            start += 1
            end -=1
        return alist



test = 'abcdefg'
s = Solution2()
print(s.LeftRotateString(test, 2))
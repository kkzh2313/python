'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，
但是与"aa.a"和"ab*a"均不匹配
'''

'''
思路：---------zhuyi：匹配的时候还需要满足原字符串没遍历完
    字符匹配的情况为：字符串的当前字符与模式的当前字符相等，或者模式的当前字符为‘.’
一。当模式中的第二个字符不是“*”时：
    1、如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，然后匹配剩余的。
    2、如果 字符串第一个字符和模式中的第一个字符相不匹配，直接返回false。
二。当模式中的第二个字符是“*”时：
如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，（相当于将模式串该位字符省略）继续匹配。
如果字符串第一个字符跟模式第一个字符匹配，可以有2种走法：
    1、字符串位置不变，模式后移2字符，相当于x*被忽略；
    2 字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位；
'''

# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if s == None or pattern == None:
            return False
        strIndex = 0
        patternIndex = 0
        return self.matchcore(s,strIndex,pattern,patternIndex)

    def matchcore(self,str,strIndex,pattern,patternIndex):
        slen = len(str)
        plen = len(pattern)
        #有效检查，str到达最后，pattern也到达最后，匹配成功
        if strIndex == slen and patternIndex == plen:
            return True
        #模式串先到尾部，遍历完全部字符，匹配失败
        if (strIndex != slen and patternIndex == plen):
            return False
        #一。模式第2个是*，
        if patternIndex+1 < plen and pattern[patternIndex+1] == '*':    #-----必须加上patternIndex+1也要在串的范围内，不然有时候会报错IndexError: string index out of range
            #1如果当前字符匹配
            #匹配的同时也要保证字符串本身没有全部遍历完
            if (strIndex < slen and str[strIndex]==pattern[patternIndex]) or (strIndex < slen and  pattern[patternIndex]=='.'):
                return self.matchcore(str,strIndex+1,pattern,patternIndex) or self.matchcore(str,strIndex,pattern,patternIndex+2)
            #不匹配就省略模式串该位，即后移两位
            else:
                return self.matchcore(str,strIndex,pattern,patternIndex+2)
        #二。模式的第二个字符不为‘*’
        # 如果匹配就是正常两个串同时后移一位
        if (strIndex < slen and str[strIndex] == pattern[patternIndex]) or (strIndex < slen and pattern[patternIndex] == '.'):
            return self.matchcore(str,strIndex+1,pattern,patternIndex+1)
        return False

s = Solution()
str = 'aa'
p = 'aa'
print(s.match(str, p))
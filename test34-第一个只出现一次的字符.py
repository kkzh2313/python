'''
题目描述
在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
'''



class Solution:
    def FirstNotRepeatingChar(self, s):
        return s.index(list(filter(lambda c:s.count(c)==1,s))[0]) if s else -1

class Solution2:
    def FirstNotRepeatingChar(self, s):
        if s == None or len(s)<=0:
            return -1
        dict = {}
        # s = list(s)#
        #第一次遍历字符串，建立起字典结构体，，时间复杂度 O(n)
        for i in s:
            if i not in dict.keys():#如果字母不在字典中，就让该字母做键  其对应得value初始为0，
                dict[i] = 0
            dict[i] +=1 #该键对应的值加1
        #第二次遍历字符串，找出字典中该字母对应得值是否为1，第一次找到就返回。时间复杂度 O(1)
        for i in s:
            if dict[i]==1:
                return s.index(i)
        return -1


s=Solution2()
a='abaccdeff'
a1='abcdef'
a2=''
a3='aabbccdd'#举这个例子时，第一种方法出现越界问题
a4=None
print(s.FirstNotRepeatingChar(a4))
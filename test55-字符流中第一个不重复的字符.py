'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。
'''

'''建立两个辅助数组，一个是字典（哈希表），一个是队列形式。
注意这里的char是指一个字符 不是字符串
1、char已经存在于字典就对应的值加1，不存在就放进字典对应值设为1，同时将字符也放进队列里  （队列里放的字符都是独一的）
2、字符流传输完，如果队列不为空且队列的首字符对应的键值不为1就将队列首字符弹出 ，继续下面的字符重复操作（操作后，队列里的字符在字典中的键值都为1，即只出现一次）
如果队列已经是空的 ，说明没有单一字符出现
否则返回队列头字符就是第一个只出现一次的字符

'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.adict = {}
        self.alist = []
    def FirstAppearingOnce(self):
        while len(self.alist)>0 and self.adict[self.alist[0]] != 1:
            self.alist.pop(0)
        if len(self.alist)==0:
            return '#'
        else:
            return self.alist[0]

    def Insert(self, char):
        if char not in self.adict.keys():
            self.adict[char] = 1
            self.alist.append(char)
        else:
            self.adict[char] += 1
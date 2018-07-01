'''
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack =[]
    def push(self, node):
        # write code here
        self.stack.append(node)#stack正常入栈
        #minstack入栈要区分两种情况：
        if self.minstack==[] or node<self.min():
            self.minstack.append(node)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self):
        if self.stack == [] or self.minstack == []:
            return None
        self.stack.pop(-1)
        self.minstack.pop(-1)

    def top(self):
        return self.stack[-1]
    def min(self):
        return self.minstack[-1]

s= Solution()
s.push(3)
print(s.min())
s.push(4)
print(s.min())
s.push(2)
print(s.min())
s.push(1)
print(s.min())
s.pop()
print(s.min())
s.pop()
print(s.min())
s.push(0)
print(s.min())
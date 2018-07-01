#########用两个栈实现队列

'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。
 队列中的元素为int类型。
'''
'''
1/用两个栈实现一个队列的功能?要求给出算法和思路!
<分析>：
入队：将元素进栈A
出队：判断栈B是否为空，如果为空，则将栈A中所有元素pop，并push进栈B，栈B出栈；
    如果不为空，栈B直接出栈。

2/用两个队列实现一个栈的功能?要求给出算法和思路!
<分析>：
入栈：将元素进队列A
出栈：判断队列A中元素的个数是否为1，如果等于1，则出队列，
否则将队列A中的元素   
以此出队列并放入队列B，直到队列A中的元素留下一个，
然后队列A出队列，再把   队列B中的元素出队列以此放入队列A中。
'''

###借助list的attend方法和pop方法
# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self,node):
        self.stack1.append(node)
    def pop(self):
        if len(self.stack1)==0 and len(self.stack2)==0:
            return
        if len(self.stack2)==0:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
class solutionQueue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self,node):
        self.queue1.append(node)
    def pop(self):
        if len(self.queue1)==0 and len(self.queue2)==0:
            return
        if len(self.queue1)==1 and len(self.queue2)==0:
            return self.queue1.pop()
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.pop(0))
        nodePop = self.queue1.pop(0)
        while len(self.queue2)>0:
            self.queue1.append(self.queue2.pop(0))
        return nodePop

if __name__ == '__main__':

    p=Solution()
    p.push(10)
    p.push(11)
    p.push(12)
    print(p.pop())

    p.push(13)
    print(p.pop())
    print(p.pop())
    print(p.pop())
    print(p.pop())

    #两个队列模拟栈的方法
    s = solutionQueue()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())

    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

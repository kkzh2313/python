# -*- coding:utf-8 -*-

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
# write code here
        if k>len(tinput):
            return []
        result=[]
        for i in range(k):
            min1=min(tinput)
            index1 = tinput.index(min1)
            result.append(tinput.pop(index1))
        return result
in1=input()
n,k=in1.strip().split(' ')
k=int(k)

in2=input()
mylist=in2.strip().split(' ')
mylist = list(map(lambda x:int(x), mylist))
s=Solution()
result=s.GetLeastNumbers_Solution(mylist,k)
result = list(map(lambda x:str(x), result))
#result=','.join(result)

#result=','.join(result)
print(result)
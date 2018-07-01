'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''


class Solution:
    ####fangfayi方法一  # 使用append一次遍历即可替换
# 由于list的append是O(1)的时间复杂度，除了扩容所导致的时间损耗，该算法复杂度为O(n)
#    join()：    连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
    def replaceSpaceByAppend(self, s):
        string=list(s)
        stringReplace = []
        for item in string:
            if item== ' ':
                stringReplace.append('%20')
            else:
                stringReplace.append(item)
        return ''.join(stringReplace)
    #方法2
    # 简单代码替换
    # 在Python中str类型是不可变的类型, 使用replace语句会生成一个新的str, 原始的s还是带空格的str变量
    def replace2(self,s):
        if type(s)!=str or len(s)<=0:
            return False
        else:
            return s.replace(' ','%20')

'''
/*
问题1：替换字符串，是在原来的字符串上做替换，还是新开辟一个字符串做替换！
问题2：在当前字符串替换，怎么替换才更有效率（不考虑java里现有的replace方法）。
      从前往后替换，后面的字符要不断往后移动，要多次移动，所以效率低下
      从后往前，先计算需要多少空间，然后从后往前移动，则每个字符只为移动一次，这样效率更高一点。
*/'''
class Solution2:
    def replaceSpaceByAppend(self, s):
        if not isinstance(s,str) or len(s)<1 or s == None:
            return ''
        #统计字符串中空格的数目，以确定字符串待扩展长度
        spacenum = 0
        for i in s:
            if i == ' ':
                spacenum += 1
        indexold = len(s)-1 #旧字符串索引位置
        newlength = len(s)+spacenum*2
        newS = [None]*newlength   #因为Python不能在字符串本身上进行扩展，这里只能新建一个新的
        indexnew = newlength-1
        while indexold>=0 and indexnew>=indexold:
            if s[indexold] == ' ':
                newS[indexnew-2:indexnew+1] = ['%','2','0']
                indexnew -= 3
                indexold -= 1
            else:
                newS[indexnew] = s[indexold]
                indexnew -= 1
                indexold -= 1
        return ''.join(newS)
if __name__ == '__main__':

    s='we are happy'
    test=Solution()
    test2 = Solution2()
    print(test.replaceSpaceByAppend(s))
    print(test2.replaceSpaceByAppend(s))
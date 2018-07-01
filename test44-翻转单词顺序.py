'''
输入一个英文句子, 翻转句子中单词的顺序,但单词内字符的顺序不变
为简单起见, 标点符号和普通字母一样处理
'''
#fangfa一 ，利用python的方法
class Solution:
    def ReverseSentence(self, s):
        if s == None or len(s)<=0:
            return ''
        l = s.split(' ')  #字符串句子按照空格进行切割
        return ' '.join(l[::-1])

#方法二  一个个字母的处理方式
'''
这个思路很简单的，从前往后一直读取，遇到空格之后就把之前读取到的压到结果的前面并添加上空格。
最后当循环结束，如果那个用来读取的字符串不为空，那么就再把它压到结果前，这次就不用再结果的最前面加空格了，
这应该就是思路吧，开始我也这么想不过觉得太朴素了，不够酷炫，后来想了想。
这个的时间复杂度会低一点，不过额外多用点内存。'''
class Solution2:
    def ReverseSentence(self, s):
        cur = ''#定义一个新的字符串存放当前处理的单词
        res = ''#定义一个字符串---存放翻转后的句子
        index = 0
        while index < len(s):
            if s[index] == ' ':
                res = ' '+ cur +res
                cur = ''
            else:
                cur += s[index]
            index += 1
        if len(cur):
            res = cur + res
        return res

#解法3 剑指offer上的  翻转两次的思路

class Solution3:
    def ReverseSentence(self, s):
        if s == None or len(s)<=0:
            return ''
        #翻转是对列表的元素进行，所以要将字符串转化为列表形式，（每个元素对应一个字母）
        strlist = list(s)
        strlist = self.Reverse(strlist) #翻转整个句子的字母

        resultstr = '' #存放最终的结果
        newlist = []  # 存放翻转后的单词, 每个元素是一个列表 ，里面对应一个单词的字母
        #定义两个指针，确定一个单词的首末位置，  注意对空格条件的处理
        begin = 0
        end = 0
        while end < len(s):
            # 遍历到句子最后位置，直接将最后的翻转单词保存到新列表里,跳出循环
            if end == len(s)-1:
                newlist.append(self.Reverse(strlist[begin:]))
                break
            # 1 这个判断语句位置需要靠前, 用来鉴定字符串开头是否是空格的情况
            # 另外遍历句子中的空格保存到新列表，两个指针同时后移
            if strlist[begin]== ' ':
                newlist.append(' ')
                begin += 1
                end += 1
            # 2 遍历到空格时，就是一个单词的结束，对这个单词进行翻转保存到新列表里.然后头指针变为尾指针位置 继续
            elif strlist[end] == ' ':
                newlist.append(self.Reverse(strlist[begin:end]))
                begin = end
            # 3 遍历到字母（还没到一个单词的结束），尾指针就继续后移
            else:
                end += 1
        for i in newlist:
            resultstr += ''.join(i)
        return resultstr


    def Reverse(self, alist):
        if alist == None or len(alist)<=0:
            return ''
        start = 0
        end = len(alist)-1
        while start < end:
            alist[start],alist[end] = alist[end],alist[start]
            start += 1
            end -=1
        return alist





str = 'I am a student.'
s = Solution3()
print(s.ReverseSentence(str))

'''
题目描述:
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
class Solution:
    def Permutation(self,ss):
        if ss == None:
            return []
        if len(ss)==1:
            return [ss]
        result = []
        for i in range(len(ss)):
            s = self.Permutation(ss[:i]+ss[i+1:])#对第i个字符外的其余字符串进行排列
            result += [ss[i]+j for j in s]#将该i字符跟其余字符串排列情况进行拼接，最后加到result列表里
        return sorted(set(result))

# ss ='abc'
# S = Solution()
# print(S.Permutation(ss))

#编写输入样例，第一行输入n--表示输入几个字符串进行判定
#第2行开始---为输入的字符串
#
n = int(input())

String = []#存放多个输入的字符串
for i in range(n):
    Input_s = input()  # 输入字符串，每输完一个用回车输入下一个
    Input_s = Input_s.strip() #就是字符串形式不需要转化
    String.append(Input_s)

s=Solution()
for i in String:
    print(s.Permutation(i))


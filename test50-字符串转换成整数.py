'''
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数
数值为0或者字符串不是一个合法的数值则返回0
'''

'''边界条件:
数据上下 溢出
空字符串
只有正负号
有无正负号
错误标志输出 
'''
# -*- coding:utf-8 -*-
class Solution:
    # 如果输出是0, 通过检查flag判断输入不合法还是输入直接是'0'
    def StrToInt(self, s):
        flag = False
        #1首先判断字符串s整体是否为空或没有字符：
        if s == None or len(s)<1:
            return 0
        # 2 d定义数组及字典（字符与数字的对应关系）
        numlist = []  # 定义一个数组，存放s中的数字
        dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}#定义
        #3 将s 中的纯数字读取到数组中
        # for i in s:
        #     if i in dict.keys(): #属于数字的放进列表
        #         numlist.append(dict[i])
        #     elif (i == '+' or i == '-') :  #字符串中的+ —的忽略
        #         continue
        #     else:                 #字符是其他类型的，为错误标志，
        #         return 0

        #下面的代码相对上面可以处理‘1234-56’这种正负号出现在字符串里面的非法标志
        index = 0
        while index < len(s):
            ss = s[index] #对字符串对应位置的字符进行下面的操作
            if ss in dict.keys():
                numlist.append(dict[ss])
            elif (ss == '+' or ss == '-') and index == 0:  # 字符串中的开头的+ —忽略
                index += 1 #------别漏了 不然无限循环
                continue
            else:                 #字符是其他类型的，为错误标志，
                return 0
            index += 1
        # 4 组合列表中的数字成一个完整的整数
        if len(numlist)==0:  #如果上述列表为空，即没有字符串中没有数字，（只有'+''-'这种）
            return 0
        num = 0
        ##4.1 若整数就是0，标志改变一下  区分非法字符的情况
        if len(numlist)==1 and numlist[0]==0:
            flag = True
            return 0
        ##4.2正数情况
        for i in numlist:
            num = num*10 + i
        ##4.3负数情况，即字符串的第一个就是’-‘
        if s[0]=='-':
            num = 0-num
        return num
s= Solution()
str='14-25'
str1= '-0000'
print(s.StrToInt(str1))
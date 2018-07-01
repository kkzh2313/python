'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''
#这道题的关键也在于讨论清楚情况，把所有可能出现的情况都考虑到。
# 需要注意的是，指数E后面必须跟一个整数，不能没有数，也不能为小数。

'''
*A.Be*C   *--表示可以为+ -， A 整数---可以不存在，B 小数---，C 指数部分
注意
1.e . 两个符号只能出现一次，
2、+ - 可以出现两次、一次、零次，一次在A前面（最开始），一次在C前面（e后面）
3、e 只能在.后面出现 ，且后面C不能为空，前面也必须有数

思路：(如果存在e)以e为边界将字符分成前后两节。依次按照下面条件判断两节是否符合要求
小数点只能在前半截，且个数是1或0；正负号只能在两节的首位置；
（两节判断情况相同的东西放在一个函数里）
'''
class Solution:
    def isNumeric(self, s):
        if s == None or len(s)<1:
            return False
        alist = [i.lower() for i in s] #转成小写
        ###------------------------------------
        # 补充后面的误判情况的判断
        if s == '+' or s=='-' or s==',':
            return False
        ###---------------------------------------
        num_e = 0
        #统计e的个数
        for i in alist:
            if i == 'e':
                num_e +=1
        if num_e >1:
            return False

        if 'e' in alist:
            #以e为边界分成两节
            index_e = alist.index('e')
            front = alist[:index_e]
            behind = alist[index_e+1:]
            ##--------下面是检测e的前后是否含有数字，没有就判断为错
            numlist = ['0','1','2','3','4','5','6','7','8','9']
            for i in front :
                if i not in numlist:
                    return False
            for i in behind:
                if i not in numlist:
                    return False

            #确保e后面没有小数点,且e后面有数
            if ('.' in behind) or len(behind)==0:
                return False
            isfront = self.scanDigit(front)
            isbehind = self.scanDigit(behind)
            return isbehind and isfront
        else:
            isNum = self.scanDigit(alist)
            return isNum


    def scanDigit(self,alist):
        point = 0 #小数点的个数
        valueTrue = ['0','1','2','3','4','5','6','7','8','9','+','-','.','e']
        for i in range(len(alist)):
            if alist[i] not in valueTrue:#存在其他的字符就为错
                return False
            if alist[i] == '.':  #统计小数点的个数
                point += 1
            if alist[i] in '+-' and i != 0:
                return False
        if point > 1:  #小数点个数多于一个为错
            return False
        return True
s = Solution()
str1 = '2e+'
print(s.isNumeric(str1))
#以下的情况应该为错，却判断对了  ，即输入’+—.‘中的单个会误判；e前面没有数字会误判；e后面没有整数会误判
# .e2    1.e+   ,+ ，-, ., e2, +.e2


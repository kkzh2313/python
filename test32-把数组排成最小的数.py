'''
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

'''
https://www.cnblogs.com/cnhkzyy/p/8678996.html sort()函数介绍
Python2 中sorted(iterable, cmp=None, key=None, reverse=False) ，Python3没有cmp参数了
参数： 
- iterable可以是list或者iterator； 
- cmp是带两个参数的比较函数； 
- key 是带一个参数的函数； 
- reverse为False或者True；

'''
#python3
class Solution:
    def PrintMinNumber(self, numbers):
        if numbers == None or len(numbers)<=0:
            return ''
        strList = list(map(str,numbers))#防止大数问题，将数组里的数字都变成字符
        from funtools import cmp_to_key
        key = cmp_to_key(lambda x,y:int(x+y)-int(y+x))
        strList.sort(key=key)
        return ''.join(strList)

# 链接：https://www.nowcoder.com/questionTerminal/8fecd3f8ba334add803bf2a06af1b993
# 来源：牛客网

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers: return ""
        numbers = list(map(str, numbers))
        numbers.sort(cmp=lambda x, y: cmp(x + y, y + x))
        return "".join(numbers).lstrip('0') or'0'
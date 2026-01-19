# Last updated: 6/2/2026, 12:05:31 PM
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        is_negative=False
        a=len(s)
        nums=[]
        nlist=0
        for i in range(a):
            if s[i]==' ' and nlist==0:
                continue
            elif s[i]=='-' and nlist==0:
                nlist+=1
                is_negative=True
            elif s[i]=='+' and nlist==0:
                nlist+=1
                continue
            elif s[i]=='0' and len(nums)==0:
                nlist+=1
                continue
            elif s[i].isdigit():
                nums.append(s[i])
                nlist+=1
            else:
                break
        if not nums:
            return 0
        num=int(''.join(nums))
        if is_negative:
            num = -num
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
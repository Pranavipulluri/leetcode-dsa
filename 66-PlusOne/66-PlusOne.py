# Last updated: 6/2/2026, 12:04:06 PM
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in digits:
            num=num*10+i
        num+=1
        new_digits=[]
        while num!=0:
            dig=num%10
            new_digits.append(dig)
            num=num//10
        return new_digits[::-1]

# Last updated: 6/2/2026, 12:02:06 PM
class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=0
        p=1
        dup=n
        while dup>0:
            digit=dup%10
            s+=digit
            p*=digit
            dup=dup//10
        div=s+p
        return div!=0 and n%div==0
        
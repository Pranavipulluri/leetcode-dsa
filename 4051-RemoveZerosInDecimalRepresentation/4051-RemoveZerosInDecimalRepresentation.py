# Last updated: 6/2/2026, 12:01:45 PM
class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(n)
        n2=""
        for ch in n:
            if ch!='0':
                n2+=ch
        return int(n2)        
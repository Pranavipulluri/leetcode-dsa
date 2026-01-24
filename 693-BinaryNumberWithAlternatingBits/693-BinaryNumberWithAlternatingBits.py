# Last updated: 6/2/2026, 12:02:38 PM
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b=bin(n)[2:]
        past=b[0]
        for i in b[1:]:
            if i==past:
                return False
            past=i
        return True
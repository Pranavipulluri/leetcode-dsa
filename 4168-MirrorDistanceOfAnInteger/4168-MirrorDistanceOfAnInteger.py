# Last updated: 6/2/2026, 12:01:01 PM
class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev=int(str(n)[::-1])
        return abs(n-rev)
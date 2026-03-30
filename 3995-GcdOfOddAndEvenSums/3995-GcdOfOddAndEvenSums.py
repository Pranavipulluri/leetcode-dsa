# Last updated: 6/2/2026, 12:01:53 PM
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        es=(n+1)*n
        os=n*n
        while es:
            os,es=es,os%es
        return os
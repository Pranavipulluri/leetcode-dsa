# Last updated: 6/2/2026, 12:00:56 PM
class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s1=s[:k]
        s2=s1[::-1]+s[k:]
        return s2
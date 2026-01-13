# Last updated: 6/2/2026, 12:05:30 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        x=str(x)
        if x!=x[::-1]:
            return False
        return True
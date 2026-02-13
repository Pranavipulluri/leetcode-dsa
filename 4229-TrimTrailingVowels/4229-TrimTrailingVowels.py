# Last updated: 6/2/2026, 12:00:40 PM
class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=len(s)-1
        while i>=0 and s[i] in "aeiou":
            i-=1
        return s[:i+1]
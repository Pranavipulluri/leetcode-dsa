# Last updated: 7/2/2026, 10:22:43 PM
1class Solution(object):
2    def isPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        s=s.lower()
8        s1=''
9        for c in s:
10            if c.isalnum():
11                s1+=c
12        return s1[::]==s1[::-1]
13            
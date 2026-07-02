# Last updated: 7/2/2026, 10:27:00 PM
1class Solution(object):
2    def isPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        s=s.lower()
8        l=0
9        r=len(s)-1
10        while l<r:
11            if not s[l].isalnum():
12                l+=1
13            elif not s[r].isalnum():
14                r-=1
15            elif s[l]==s[r]:
16                l+=1
17                r-=1
18            else:
19                return False
20        return True
21
22            
23            
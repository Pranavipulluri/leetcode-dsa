# Last updated: 6/4/2026, 10:52:03 AM
# even and odd check separate always for palindrom and expand on both sides for each element
1class Solution(object):
2    def countSubstrings(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        n=len(s)
8        res=0
9        for i in range(n):
10            l=i
11            r=i
12            while l>=0 and r<n and s[l]==s[r]:
13                res+=1
14                l-=1
15                r+=1
16        for i in range(n-1):
17            l=i
18            r=i+1
19            while l>=0 and r<n and s[l]==s[r]:
20                res+=1
21                l-=1
22                r+=1
23        return res
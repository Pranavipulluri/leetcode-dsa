# Last updated: 7/5/2026, 10:48:29 PM
1from collections import defaultdict
2class Solution(object):
3    def minWindow(self, s, t):
4        """
5        :type s: str
6        :type t: str
7        :rtype: str
8        """
9        start=0
10        needed=defaultdict(int)
11        window=(0,float('inf'))
12        for ch in t:
13            needed[ch]+=1
14        need=len(t)
15        for end in range(len(s)):
16            if s[end] in needed:
17                if needed[s[end]]>0:
18                    need-=1
19                needed[s[end]]-=1
20            while need==0:
21                if end - start < window[1] - window[0]:
22                    window = (start, end)
23                if s[start] in needed:
24                    needed[s[start]]+=1
25                    if needed[s[start]]>0:
26                        need+=1
27                start+=1
28        if window[1] == float('inf'):
29            return ""
30        return s[window[0]:window[1]+1]
31
# Last updated: 7/6/2026, 10:45:02 PM
1class Solution(object):
2    def checkInclusion(self, s1, s2):
3        """
4        :type s1: str
5        :type s2: str
6        :rtype: bool
7        """
8        freq=defaultdict(int)
9        for i in s1:
10            freq[i]+=1
11        n=len(s1)
12        i=0
13        if n>len(s2):
14            return False
15        for j in range(n):
16            if s2[j] in freq:
17                freq[s2[j]]-=1
18        if all(v == 0 for v in freq.values()):
19            return True
20        for j in range(n,len(s2)):
21            if s2[j] in freq:
22                freq[s2[j]]-=1
23            if s2[i] in freq:
24                freq[s2[i]]+=1
25            i+=1
26            if all(v == 0 for v in freq.values()):
27                return True
28        return False
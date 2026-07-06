# Last updated: 7/6/2026, 10:36:50 PM
1class Solution(object):
2    def characterReplacement(self, s, k):
3        """
4        :type s: str
5        :type k: int
6        :rtype: int
7        """
8        res=0
9        freq=defaultdict(int)
10        i=0
11        for j in range(len(s)):
12            freq[s[j]]+=1
13            maxFreq=max(freq.values())
14            curLen=j-i+1
15            if curLen-maxFreq>k:
16                freq[s[i]]-=1
17                i+=1
18            res=max(res,j-i+1)
19        return res
20
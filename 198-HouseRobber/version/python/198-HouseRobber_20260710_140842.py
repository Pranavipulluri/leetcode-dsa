# Last updated: 7/10/2026, 2:08:42 PM
1class Solution(object):
2    def rob(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        rob1=0
8        rob2=0
9        for n in nums:
10            temp=max(n+rob1,rob2)
11            rob1=rob2
12            rob2=temp
13        return max(rob1,rob2)
# Last updated: 6/3/2026, 11:51:45 PM
1class Solution(object):
2    def rob(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        def helper(nums):
8            rob1=0
9            rob2=0
10            for n in nums:
11                temp=max(n+rob1,rob2)
12                rob1=rob2
13                rob2=temp
14            return max(rob1,rob2)
15        return max(nums[0],helper(nums[1:]),helper(nums[:-1]))
16        
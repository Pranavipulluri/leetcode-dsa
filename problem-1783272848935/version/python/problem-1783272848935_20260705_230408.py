# Last updated: 7/5/2026, 11:04:08 PM
1class Solution(object):
2    def minSubArrayLen(self, target, nums):
3        """
4        :type target: int
5        :type nums: List[int]
6        :rtype: int
7        """
8        if max(nums)>=target:
9            return 1
10        start=0
11        total=0
12        window=float('inf')
13        for end in range(len(nums)):
14            total+=nums[end]
15            while total>=target:
16                if window>end-start+1:
17                    window=end-start+1
18                total-=nums[start]
19                start+=1
20        return window if window!=float('inf') else 0
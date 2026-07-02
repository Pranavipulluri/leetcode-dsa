# Last updated: 7/2/2026, 4:41:45 PM
1class Solution(object):
2    def majorityElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        nums.sort()
8        n=len(nums)//2
9        return nums[n]
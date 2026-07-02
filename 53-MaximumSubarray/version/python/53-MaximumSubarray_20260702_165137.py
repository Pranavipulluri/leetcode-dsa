# Last updated: 7/2/2026, 4:51:37 PM
1class Solution(object):
2    def rotate(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: None Do not return anything, modify nums in-place instead.
7        """
8        n=len(nums)
9        k=k%n
10        arr1=nums[-k::]
11        nums[:]=arr1+nums[:-k]
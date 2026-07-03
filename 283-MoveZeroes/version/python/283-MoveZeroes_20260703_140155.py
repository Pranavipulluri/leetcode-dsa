# Last updated: 7/3/2026, 2:01:55 PM
1class Solution(object):
2    def moveZeroes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7        k=0
8        n=len(nums)
9        for i in range(n):
10            if nums[i]!=0:
11                nums[k]=nums[i]
12                k+=1
13        for i in range(k,n):
14            nums[i]=0
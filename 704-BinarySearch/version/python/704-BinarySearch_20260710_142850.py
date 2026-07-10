# Last updated: 7/10/2026, 2:28:50 PM
1class Solution(object):
2    def search(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        left=0
9        right=len(nums)-1
10        while left<=right:
11            mid=(left+right)//2
12            if nums[mid]==target:
13                return mid
14            elif nums[mid]>target:
15                right=mid-1
16            else:
17                left=mid+1
18        return -1
19
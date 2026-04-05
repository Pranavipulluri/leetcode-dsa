# Last updated: 6/2/2026, 12:02:10 PM
class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        s = 0
        nums.sort()
        l, r = 0, len(nums) - 1

        while l < r - 1:
            s += nums[r - 1]  
            l += 1           
            r -= 2           
        return s
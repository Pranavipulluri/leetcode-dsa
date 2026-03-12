# Last updated: 6/2/2026, 12:01:23 PM
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[abs(x) for x in nums]
        nums.sort()
        a=nums[-1]
        b=nums[-2]
        return a*b*100000
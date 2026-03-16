# Last updated: 6/2/2026, 12:01:29 PM
class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            if k*(i+1) not in nums:
                return k*(i+1)
        return k*(n+1)
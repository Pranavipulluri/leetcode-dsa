# Last updated: 6/2/2026, 12:00:38 PM
class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dom=0
        s=sum(nums)
        n=len(nums)
        for i in range(n-1):
            s-=nums[i]
            if nums[i]*(n-1-i)>s:
                dom+=1
        return dom
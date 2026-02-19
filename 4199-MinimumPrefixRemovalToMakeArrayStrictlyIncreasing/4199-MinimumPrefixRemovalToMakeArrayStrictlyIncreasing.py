# Last updated: 6/2/2026, 12:00:47 PM
class Solution(object):
    def minimumPrefixLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[i-1]:
                continue
            else:
                ans=i
                break
        return ans
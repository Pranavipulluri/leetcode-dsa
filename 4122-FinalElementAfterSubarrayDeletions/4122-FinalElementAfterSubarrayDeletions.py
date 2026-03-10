# Last updated: 6/2/2026, 12:01:16 PM
class Solution(object):
    def finalElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[0]
        ans=max(nums[0],nums[-1])
        if n>2:
            max_mid=max(nums[1:-1])
            ans=max(ans,min(max_mid,nums[-1]))
            ans=max(ans,min(max_mid,nums[0]))
        return ans
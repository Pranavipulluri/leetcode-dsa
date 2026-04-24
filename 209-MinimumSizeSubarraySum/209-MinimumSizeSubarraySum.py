# Last updated: 6/2/2026, 12:02:50 PM
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        cur_sum=0
        res=float('inf')
        for r in range(len(nums)):
            cur_sum+=nums[r]
            while cur_sum>=target:
                res=min(res,r-l+1)
                cur_sum-=nums[l]
                l+=1
        return 0 if res==float('inf') else res
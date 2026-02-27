# Last updated: 6/2/2026, 12:00:59 PM
class Solution(object):
    def maximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        smin=[0]*n
        smin[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            smin[i]=min(nums[i],smin[i+1])
        psum=0
        ans=float('-inf')
        for i in range(n-1):
            psum+=nums[i]
            curr=psum-smin[i+1]
            ans=max(ans,curr)
        return ans
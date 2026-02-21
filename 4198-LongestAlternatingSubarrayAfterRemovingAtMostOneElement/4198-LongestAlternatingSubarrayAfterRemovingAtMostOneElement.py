# Last updated: 6/2/2026, 12:00:48 PM
class Solution(object):
    def longestAlternating(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return 1
        dp=[[1]*2 for _ in range(n)]
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[i][0]=dp[i-1][1]+1
            if nums[i]<nums[i-1]:
                dp[i][1]=dp[i-1][0]+1
        rdp=[[1]*2 for _ in range(n)]
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                rdp[i][0]=rdp[i+1][1]+1
            if nums[i]>nums[i+1]:
                rdp[i][1]=rdp[i+1][0]+1
        ans=max(max(row) for row in dp)
        for i in range(1,n-1):
            if nums[i-1]<nums[i+1]:
                ans=max(ans,dp[i-1][1]+rdp[i+1][1])
            if nums[i-1]>nums[i+1]:
                ans=max(ans,dp[i-1][0]+rdp[i+1][0])
        return ans